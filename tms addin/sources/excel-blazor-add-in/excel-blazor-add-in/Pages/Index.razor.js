/* Copyright(c) Maarten van Stam. All rights reserved. Licensed under the MIT License. */
/**
 * Basic function to show how to insert a value into cell A1 on the selected Excel worksheet.
 */
export function helloButton() {

    return Excel.run(context => {

        // Insert text 'Hello world!' into cell A1.
        context.workbook.worksheets.getActiveWorksheet().getRange("A1").values = [['Hello world!']];

        // sync the context to run the previous API call, and return.
        return context.sync();
    });
}

export function userButton() {

    try {
        let accessToken = await Office.auth.getAccessToken();
        console.log(accessToken);

        let tokenData = await OfficeRuntime.auth.getAccessToken({ allowSignInPrompt: false, forMSGraphAccess: true });
        var parts = tokenData.split(".");
        var token = JSON.parse(atob(parts[1]));
        console.log(token.preferred_username);
        return token.preferred_username;
    }
    catch (exception) {
        console.log(exception.message);
    }
}