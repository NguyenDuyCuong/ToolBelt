import {Component} from '@angular/core';

declare const Excel: any;
declare const Office: any;

@Component({
    selector: 'app-blank',
    templateUrl: './blank.component.html',
    styleUrls: ['./blank.component.scss']
})
export class BlankComponent {
    onColorMe() {
        Excel.run(async (context) => {
          const range = context.workbook.getSelectedRange();
          range.format.fill.color = 'green';
          await context.sync();
        });
    }

    async getIDToken() {
        try {
          let userTokenEncoded = await Office.auth.getAccessToken({
            allowSignInPrompt: true,
          });
          console.log(userTokenEncoded);
        } catch (error) {
          console.log(error);
        }
    }
}
