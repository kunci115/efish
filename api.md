**Accounts**
----
  Url will be written with production ip, if you run it locally, just change it to "localhost" Returns json data about a single user.

* **URL Production Register**

  128.199.106.148:8000/account/register/

    * **Method:**

      `POST`
      
    *  **URL Params**
    
       **Required:**
     
       `phone_number=[integer]` <br>
       `role=[char]` <br>
       `name=[char]`
    
    * **Data Params**
    
      * **Body Sample Call**
        ```
          {"phone_number":"62812823123",
          "role":"admin",
          "name":"John"}
        ```
    
    * **Success Response:**
    
      * **Code:** 201 <br />
        **Content:** `{ password: [generated password]}`
        
      * **Code:** 200 <br />
        **Content:** `{error: "Phone Number Already Taken"}`'
     
    * **Error Response:**
    
      * **Code:** 400 Bad Request <br />
        **Content:** `{ field : "This field is required" }`
<br><br><br>
* **URL Production Login**

  128.199.106.148:8000/account/register/

    * **Method:**

      `POST`

    *  **URL Params**

       **Required:**

       `phone_number=[integer]` <br>
       `password=[char]`

    * **Data Params**

        * **Body Sample Call**
          ```
            {
              "phone_number":"62812823123",
              "password":"test"
            }
          ```

    * **Success Response:**

        * **Code:** 201 <br />
          **Content:** `{ "jwt": [generated jwt]}`

    * **Error Response:**

        * **Code:** 400 Bad Request <br />
          **Content:** `{ field : "This field is required" }`
          <br><br><br>
* **URL Production Detail JWT**

  128.199.106.148:8000/account/jwt/

    * **Method:**

      `POST`

    *  **URL Params**

       **Required:**

       `jwt=[char]` <br>

    * **Data Params**

        * **Body Sample Call**
          ```
            {
              "jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwaG9uZV9udW1iZXIiOiIxMjM0NTY3IiwibmFtZSI6IlJpbm8gIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjE5OTY3MjkwfQ.q9o7Os2gIFCAnOVBnywutfJSMv_VBnWOyxuPdKmhKPw"
            }
          ```

    * **Success Response:**

        * **Code:** 200 <br />
          **Content:** `{
          "phone_number": "1234567",
          "name": "Rino ",
          "role": "admin",
          "exp": 1619975932
          }`

    * **Error Response:**

        * **Code:** 401 unauthorized <br />
          **Content:** `{ message : "jwt expired" }`
        * **Code:** 400 Bad Request <br />
          **Content:** `{ field : "This field is required" }`
        * **Code:** 400 Bad Request <br />
          **Content:** `{ message : "jwt not registered",
                          err: error message}`  
          <br><br><br>
* **URL Production resource(price usd)**

  128.199.106.148:3000/efish/resource

    * **Method:**

      `GET`

    *  **URL Params**

       **Required:**

       `jwt-token=[char] on header` <br>

    * **Data Params**

        * **Header Sample Call**
          ```
          curl --location --request GET '128.199.106.148:3000/efish/resource' --header 'jwt-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwaG9uZV9udW1iZXIiOiIxMjM0NTY3IiwibmFtZSI6IlJpbm8gIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjE5OTc3Mjk2fQ.7tf20wFj-T7GQgV0rOveHMerfjVm5-ILCcZOtqFePNU' --data-raw ''
          ```

    * **Success Response:**

        * **Code:** 200 <br />
          **Content:** `[ {
        "uuid": "0c192840-7ee4-11ea-b3e1-e335da5df3hj",
        "komoditas": "Cupang leher",
        "area_provinsi": "JAWA BARAT",
        "area_kota": "CIMAHI",
        "size": "101",
        "price": "20100",
        "tgl_parsed": "2021-04-20T16:19:37+07:00",
        "timestamp": "1618910377",
        "USD_price": "1.3917"
    },]`

    * **Error Response:**

        * **Code:** 401 unauthorized <br />
          **Content:** `{
                        "name": "JsonWebTokenError",
                        "message": "jwt must be provided"
                        }`
        * **Code:** 401 unauthorized <br />
          **Content:**  `{
                        "name": "TokenExpiredError",
                        "message": "jwt expired",
                        "expiredAt": "2021-05-02T14:54:50.000Z"
                    }`

          <br><br><br>
    
* **URL Production storage aggregate(provinsi, week)**

  128.199.106.148:3000/efish/storages

    * **Method:**

      `GET`

    *  **URL Params**

       **Required:**

       `jwt-token=[char] on header` <br>

    * **Data Params**

        * **Header Sample Call**
          ```
          curl --location --request GET '128.199.106.148:3000/efish/storages' --header 'jwt-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwaG9uZV9udW1iZXIiOiIxMjM0NTY3IiwibmFtZSI6IlJpbm8gIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjE5OTc3Mjk2fQ.7tf20wFj-T7GQgV0rOveHMerfjVm5-ILCcZOtqFePNU' --data-raw ''
          ```

    * **Success Response:**

        * **Code:** 200 <br />
          **Content:** `{"JAWA BARAT": {
        "2": {
            "average": "7.142864285721429e+79",
            "min": "1000.0000",
            "max": "21021.0000",
            "median": "100000.0000"
        },}`

    * **Error Response:**

        * **Code:** 401 unauthorized <br />
          **Content:** `{
                        "name": "JsonWebTokenError",
                        "message": "jwt must be provided"
                        }`
        * **Code:** 401 unauthorized <br />
          **Content:** `{
                        "name": "TokenExpiredError",
                        "message": "jwt expired",
                        "expiredAt": "2021-05-02T14:54:50.000Z"
                    }`

          <br><br><br>
* **URL Production storage aggregate(provinsi, week)**

  128.199.106.148:3000/efish/jwt

    * **Method:**

      `GET`

    *  **URL Params**

       **Required:**

       `jwt-token=[char] on header` <br>

    * **Data Params**

        * **Header Sample Call**
          ```
          curl --location --request GET '128.199.106.148:3000/efish/jwt' --header 'jwt-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwaG9uZV9udW1iZXIiOiIxMjM0NTY3IiwibmFtZSI6IlJpbm8gIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjE5OTc3Mjk2fQ.7tf20wFj-T7GQgV0rOveHMerfjVm5-ILCcZOtqFePNU' --data-raw ''
          ```

    * **Success Response:**

        * **Code:** 200 <br />
          **Content:** `{
                    "phone_number": "1234567",
                    "name": "Rino ",
                    "role": "admin",
                    "exp": 1619977928
                }`

    * **Error Response:**

        * **Code:** 401 unauthorized <br />
          **Content:** `{
                        "name": "JsonWebTokenError",
                        "message": "jwt must be provided"
                        }`
        * **Code:** 401 unauthorized <br />
          **Content:** `{
                        "name": "TokenExpiredError",
                        "message": "jwt expired",
                        "expiredAt": "2021-05-02T14:54:50.000Z"
                    }`

          <br><br><br>        