# BitCloutInfo API

To get started in using this service tool, here are the endpoints and were they relay information from along with their respective parameters too.


The Extension of the server url would be `/api/v1` followed by any of the following resources;

`/` (GET REQUEST)

-   Base bitclout resource for all meta data


`/get-block` (POST REQUEST)

-   Returns the bitclout blocks info

`/get-exchange-rate` (GET REQUEST)

-   Returns the current exchange rate

`/get-app-state` (POST REQUEST)

-   Returns the node current status

`/get-follows` (POST REQUEST)

-   Returns the followed account (Not sure)

`/get-messages` (POST REQUEST)

-   Returns messages data

`/get-notifications` (POST REQUEST)

-   Returns notifications data

`/get-posts` (POST REQUEST)

- Returns all existing posts

`/get-profiles` (POST REQUEST)

- Returns all profile data

`/get-users` (POST REQUEST)

- Returns global users data

`/get-transactions` (POST REQUEST)

- Returns trnasactions data


### ALL POST REQUIRE `PublicKeyBase58Check` & `IsMempool`(optional) AS PARAMETERS IN THE BODY OF YOUR REQUEST