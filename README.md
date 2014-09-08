


AppFeed can be used to feed data for the application specially mobile app.

Written in Python 2.7 Django Framework With MySql

You can just call in single url with procedure name and data in json format than you will get response on json

For example:

http://example.com/feed -> URL

`PROCEDURE_NAME ="insertUser"`
          
`DATA = json.dumps({"ID":88,"NAME":"Dpak Malla"})`
        
Than You will get JSON response:
      
`{"msg": "Invalid Request!", "error": true}`

