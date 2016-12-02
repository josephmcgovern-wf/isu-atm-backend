## ATM Server

To begin a new ATM session, send a request to the [start session endpoint](https://github.com/josephmcgovern-wf/isu-atm-backend/blob/master/docs/atm_api.md#start-new-atm-session).
This endpoint will respond with a `token`. This token will be used in all
other requests. You *must* include `X-Api-ATM-Key` as a header with its value
being `token`. If you do not, every request will fail. Once you have this token,
you can operate on any of the accounts belonging to the user. Once you're done
using the ATM, **do not forget to close the session!**.
