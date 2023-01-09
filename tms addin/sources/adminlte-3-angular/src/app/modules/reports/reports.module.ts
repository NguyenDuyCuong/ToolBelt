import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReportsRoutingModule } from './reports-routing.module';
import { WorkingTimeComponent } from './working-time/working-time.component';
import { LayoutComponent } from './layout/layout.component';
import { TimeCardComponent } from "../../components/time-card/time-card.component";


@NgModule({
    declarations: [
        WorkingTimeComponent,
        LayoutComponent
    ],
    imports: [
        CommonModule,
        ReportsRoutingModule,
        TimeCardComponent
    ]
})
export class ReportsModule { }
