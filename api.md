**Show User**
----
  Returns json data about a single user.

* **URL**

  /account/register

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
      "role":"Seller",
      "name":"John"}
    ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ password: [generated password]}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

