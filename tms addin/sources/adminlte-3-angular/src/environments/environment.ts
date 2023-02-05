// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
import {LogLevel} from '@azure/msal-browser';

const clientId = "79f466b0-e96f-4979-adff-702eaa717b1a";
const accessScope = "api://" + window.location.host + "/" + clientId + "/access_as_user";


export const environment = {
    production: false,
    msalConfig: {
        auth: {
          clientId: clientId, // This is the ONLY mandatory field that you need to supply.
          authority: "https://login.microsoftonline.com/common", // Defaults to "https://login.microsoftonline.com/common"
          redirectUri: "https://localhost:4200", // You must register this URI on Azure Portal/App Registration. Defaults to window.location.href
          //postLogoutRedirectUri: "https://localhost:44355/signout", // Simply remove this line if you would like navigate to index page after logout.
          navigateToLoginRequestUrl: false, // If "true", will navigate back to the original request location before processing the auth code response.
          response_type: "access_token"
        },
        cache: {
          cacheLocation: "localStorage", // Configures cache location. "sessionStorage" is more secure, but "localStorage" gives you SSO.
          storeAuthStateInCookie: false, // If you wish to store cache items in cookies as well as browser cache, set this to "true".
        },
        system: {
          loggerOptions: {
            loggerCallback: (level, message, containsPii) => {
              if (containsPii) {
                return;
              }
              switch (level) {
                case LogLevel.Error:
                  console.error(message);
                  return;
                case LogLevel.Info:
                  console.info(message);
                  return;
                case LogLevel.Verbose:
                  console.debug(message);
                  return;
                case LogLevel.Warning:
                  console.warn(message);
                  return;
              }
            }
          }
        }
    },
    loginRequest: {
        "scopes": [accessScope],
        "extraScopesToConsent": ["files.read"]
    }
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.
