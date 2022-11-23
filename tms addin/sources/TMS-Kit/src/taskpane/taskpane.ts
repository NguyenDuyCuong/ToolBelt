/*
 * Copyright (c) Microsoft Corporation. All rights reserved. Licensed under the MIT license.
 * See LICENSE in the project root for license information.
 */
import "zone.js"; // Required for Angular
import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";
import { provideFluentDesignSystem, fluentCard, fluentButton, fluentTextField } from '@fluentui/web-components';
import AppModule from "./app/app.module";

/* global console, document, Office */

Office.onReady(() => { 
  provideFluentDesignSystem().register(fluentCard(), fluentButton(), fluentTextField());

  // Bootstrap the app
  platformBrowserDynamic()
    .bootstrapModule(AppModule)
    .catch((error) => console.error(error));
});
