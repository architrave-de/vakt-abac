# vakt-abac

## How to run

* Clone the repository `git@github.com:architrave-de/vakt-abac.git`
* Run `docker-compose up -d`

##  Overview


| User        |  Group        | Authorization Token  |
| ------------- |:-------------:| -----:|
|admin@architrave.de      | admin | 10 |
|user@architrave.de    | user      |  20 |
|bidder@architrave.de | user    |    30 |

* Admin group has a FullAcessPolicy - can access all resources
* User group has OwnerAccessPolicy  – can only access and edit own resources

### How to test

#### Testing the document api
* Run the application
*  Make a POST|PUT|GET| request to `api/documents`
*  Set the authorization header with one of the authorization tokens provided in the table above.

*  Make a POST|PUT|GET| request to `api/documents/1`

#### Testing the user api

* Run the application
*  Make a POST|PUT|GET| request to `api/user`
*  Set the authorization header with one of the authorization tokens provided in the table above.

*  Make a POST|PUT|GET| request to `api/user/1`


