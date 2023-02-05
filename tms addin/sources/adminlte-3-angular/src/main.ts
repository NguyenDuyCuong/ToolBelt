import {enableProdMode, LOCALE_ID} from '@angular/core';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {Gatekeeper} from 'gatekeeper-client-sdk';
import {PublicClientApplication} from '@azure/msal-browser';

import {AppModule} from './app/app.module';
import {environment} from './environments/environment';


if (environment.production) {
    enableProdMode();
}

(window as any).PF = {
    config: {
        mode: 'bs4'
    }
};


declare const Office: any;


Gatekeeper.initialize('9966bf1b-5da5-4b55-9301-86f9f0c77aaf');
const myMSALObj = new PublicClientApplication(environment.msalConfig);


Office.initialize = async (info) => {
    if (info.host === Office.HostType.Excel) {
        // Do Excel-specific initialization (for example, make add-in task pane's
        // appearance compatible with Excel "green").
    }
    if (info.platform === Office.PlatformType.PC) {
        // Make minor layout changes in the task pane.
    }
    console.log(`Office.js is now ready in ${info.host} on ${info.platform}`);
    platformBrowserDynamic()
        .bootstrapModule(AppModule, {
            providers: [{provide: LOCALE_ID, useValue: 'en-US' }]
          })
        .catch((err) => console.error(err));
};
