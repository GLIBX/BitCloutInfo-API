# BitCloutInfo API


This is the official open-sourced API for the <a href="">MyBitcloutInfo</a> website as to be a dashboard for filter through and finding the best and most suitable sellers/ coinholders but updated reports on their total value and change over time, built on the BitClout project


# API Documentation

To get started in using this service tool, here are the endpoints and were they relay information from along with their respective parameters too.


The Extension of the server url would be `/api/v1` followed by any of the following resources;

## `/` (GET REQUEST)

-   Base bitclout resource for all meta data

## `/get-bitclout-price` (GET REQUEST ONLY)

- Returns the current price of bitclout price data


## `/get-block` (POST REQUEST)

-   Returns the bitclout blocks info
params;
1. PublicKeyBase58Check (String)
2. IsMempool (Boolean) default `false`

## `/get-exchange-rate` (GET REQUEST)

-   Returns the current exchange rate

## `/get-app-state` (POST REQUEST)

-   Returns the node current status

## `/get-follows` (POST REQUEST)

-   Returns the followed account (Not sure)
params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-messages` (POST REQUEST)

-   Returns messages data
params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-notifications` (POST REQUEST)

-   Returns notifications data

params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-posts` (POST REQUEST)

- Returns all existing posts

params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-profiles` (POST REQUEST)

- Returns all profile data

params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-users` (POST REQUEST)

- Returns global users data
params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`

## `/get-transactions` (POST REQUEST)

- Returns trnasactions data

params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`


## `/get-verified-users` (POST REQUEST)

- Returns trnasactions data

params;
1. PublicKeyBase58Check (String)
2. Username (String) or `null` to fetch all
3. UsernamePrefix (String) or `null` to fetch all
4. Description (String/null) or `null` to fetch all
5. OrderBy (String)
6. NumToFetch (Integer)
7. ReaderPublicKeyBase58Check (String)
8. ModerationType (String)
9. FetchUsersThatHODL (Boolean) default `false`
10. AddGlobalFeedBool (Boolean) default `false`


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
