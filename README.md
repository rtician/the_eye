# The Eye
ConsumerAffairs code challenge.

### Logic
- Applications should be authorized to send requests to `The Eye`. For this the app should be previously registered and have a valid `token`
- The request payload should link this:
```json
{
    "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
    "name": "pageview",
    "category": "page interaction",
    "data": {
        "host": "www.consumeraffairs.com",
        "path": "/"
    },
    "timestamp": "2021-01-01 09:15:27.243860"
}
```
- `timestamp` should be sent be the app to ensure the creation order

### How to use it?
```shell
$ git clone https://github.com/rtician/the_eye
$ cd the_eye
```

```python
In [1]: from events.models import Application

In [2]: app = Application.objects.create(name='App Name')
In [3]: print(app.token)
Out[4]: 
'1234567890abcdefghijk'
```

- Run
````shell
$ make run
````

- Make a POST request to `localhost:8080/api/events`

### Run the tests
````shell
$ make tests
````