import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReportsRoutingModule } from './reports-routing.module';
import { WorkingTimeComponent } from './working-time/working-time.component';
import { LayoutComponent } from './layout/layout.component';
import { TimeLineComponent } from "../../components/time-line/time-line.component";
import { TimeCalendarComponent } from "../../components/time-calendar/time-calendar.component";


@NgModule({
    declarations: [
        WorkingTimeComponent,
        LayoutComponent
    ],
    imports: [
        CommonModule,
        ReportsRoutingModule,
        TimeLineComponent,
        TimeCalendarComponent
    ]
})
export class ReportsModule { }
