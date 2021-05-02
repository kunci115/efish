const express = require('express')
const app = express()
const port = 3000
const fetch = require('node-fetch')
const _ = require('lodash');
var jwt = require('jsonwebtoken')
var LRU = require("lru-cache")
    , options = { max: 500
    , length: function (n, key) { return n * 2 + key.length }
    , maxAge: 1000 * 5 * 60 }
    , cache = new LRU(options)

var decoder_incoming = function(req, res, next) {
    try {
        const jwt_token = req.headers['jwt-token']
        var decoded = jwt.verify(jwt_token, 'efish-test', {algorithm: ['HS256']})
        req['decoded'] = decoded
        next()
    } catch(err) {
        res.status(401).send(err)
    }
}
function median(arr){
    arr.sort(function(a, b){ return a - b; });
    var i = arr.length / 2;
    return i % 1 == 0 ? (parseFloat(arr[i - 1]) + parseFloat(arr[i])) / 2 : parseFloat(arr[Math.floor(i)]);
}

Date.prototype.getWeek = function (dowOffset) {
    /*getWeek() was developed by Nick Baicoianu at MeanFreePath: http://www.meanfreepath.com */

    dowOffset = typeof(dowOffset) == 'int' ? dowOffset : 0; //default dowOffset to zero
    var newYear = new Date(this.getFullYear(),0,1);
    var day = newYear.getDay() - dowOffset; //the day of week the year begins on
    day = (day >= 0 ? day : day + 7);
    var daynum = Math.floor((this.getTime() - newYear.getTime() -
        (this.getTimezoneOffset()-newYear.getTimezoneOffset())*60000)/86400000) + 1;
    var weeknum;
    //if the year starts before the middle of a week
    if(day < 4) {
        weeknum = Math.floor((daynum+day-1)/7) + 1;
        if(weeknum > 52) {
            nYear = new Date(this.getFullYear() + 1,0,1);
            nday = nYear.getDay() - dowOffset;
            nday = nday >= 0 ? nday : nday + 7;
            /*if the next year starts before the middle of
              the week, it is week #1 of that year*/
            weeknum = nday < 4 ? 1 : 53;
        }
    }
    else {
        weeknum = Math.floor((daynum+day-1)/7);
    }
    return weeknum;
};

app.use(decoder_incoming)

app.get('/efish/resource', async (req, res) => {
    const data_efish = await fetch('https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list')
    const resp_data = await data_efish.json()
    var usd_idr = {'USD_IDR': 0}
    if (cache.get("conversion") === undefined){
        const conversion = await fetch('https://free.currconv.com/api/v7/convert?q=USD_IDR&compact=ultra&apiKey=4f58cd316f6c48a81912')
        usd_idr = await conversion.json()
        cache.set("conversion", usd_idr)
    }
    else {
        usd_idr = cache.get('conversion')
    }

    // console.log(usd_idr)
    for (i=0; i<resp_data.length; i++){
        if (resp_data[i]['uuid'] === null || resp_data[i]['tgl_parsed'] === null || resp_data[i]['price'] === null){
            delete resp_data[i]
            continue
        }
        if (resp_data[i]['price'] != null){
            const convert_idr_to_usd = (parseFloat(resp_data[i]['price'])/parseFloat(usd_idr['USD_IDR'])).toFixed(4)
            resp_data[i]['USD_price'] = convert_idr_to_usd
        }

    }

    res.send(resp_data.filter(Boolean))
})

app.get('/efish/storages', async (req, res) => {
    if (req['decoded']['role'] !== "admin"){
        res.json(req['decoded'])
    }
    const data_efish = await fetch('https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list')
    var mem = {}

    const resp_data = await data_efish.json()
    for (i=0; i<resp_data.length; i++) {
        var min_max_avg = []
        if (resp_data[i]['uuid'] === null || resp_data[i]['tgl_parsed'] === null || resp_data[i]['price'] === null) {
            delete resp_data[i]
            continue
        }
        if (resp_data[i]['tgl_parsed'] != null) {
            var week_counter = resp_data[i]['tgl_parsed'].substring(0, 10)
            var week = new Date(week_counter)
            resp_data[i]['week'] = week.getWeek()
        }
        if(!(resp_data[i]["area_provinsi"] in mem)){
            mem[resp_data[i]["area_provinsi"]] = {};
        }

        if(!(resp_data[i]['week'] in mem[resp_data[i]["area_provinsi"]])){
            mem[resp_data[i]["area_provinsi"]][resp_data[i]['week']] = [];
        }

        mem[resp_data[i]["area_provinsi"]][resp_data[i]['week']].push(resp_data[i]['price'])
    }
    var endResp = {}
    for(m in mem){
        endResp[m] = {}
        for(w in mem[m]){
            endResp[m][w] = {
                "average": parseFloat(_.mean(mem[m][w])).toFixed(4),
                "min": parseFloat(_.min(mem[m][w])).toFixed(4),
                "max": parseFloat(_.max(mem[m][w])).toFixed(4),
                "median": parseFloat(median(mem[m][w])).toFixed(4)
            }
        }
    }

    res.send(endResp)
})

app.get('/efish/jwt', async (req, res) => {
        res.json(req['decoded'])
}
)


app.listen(port, () => {
    console.log(`Server Listen http://localhost:${port}`)
})
