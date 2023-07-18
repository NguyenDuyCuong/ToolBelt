import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { DefaultDataService, HttpUrlGenerator } from "@ngrx/data";
import { Observable, map } from "rxjs";
import { WorkingTime } from "../models/working-time.model";


declare const Excel: any;


@Injectable()
export class WorkingTimeDataService extends DefaultDataService<WorkingTime> {


    constructor(http:HttpClient, httpUrlGenerator: HttpUrlGenerator) {
        super('WorkingTime', http, httpUrlGenerator);

    }

    getAll(): Observable<WorkingTime[]> {
        return new Observable(subscriber => {
            Excel.run(async (context) => {
                const range = context.workbook.getSelectedRange();
                range.format.fill.color = 'green';
                await context.sync();
    
                subscriber.next([]);
            });
        });
    }

}
