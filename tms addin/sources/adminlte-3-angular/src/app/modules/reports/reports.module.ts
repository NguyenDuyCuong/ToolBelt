import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReportsRoutingModule } from './reports-routing.module';
import { WorkingTimeComponent } from './working-time/working-time.component';
import { TimeCalendarComponent } from '@components/time-calendar/time-calendar.component';
import { TimeLineComponent } from '@components/time-line/time-line.component';
import { EntityDataService, EntityDefinitionService } from '@ngrx/data';
import { WorkingTimeDataService } from './services/working-time-data.service';
import { entityMetadata } from './models/entity.metadata';
import { WorkingTimeResolver } from './services/working-time.resolver';
import { WorkingTimeEntityService } from './services/working-time-entity.service';


@NgModule({
    declarations: [
        WorkingTimeComponent
    ],
    imports: [
        CommonModule,
        TimeLineComponent,
        TimeCalendarComponent,
        ReportsRoutingModule
    ],
    providers: [
        WorkingTimeEntityService,
        WorkingTimeResolver,
        WorkingTimeDataService
    ]
})
export class ReportsModule {
    constructor(
        private eds: EntityDefinitionService,
        private entityDataService: EntityDataService,
        private workingTimeDataService: WorkingTimeDataService) {

        eds.registerMetadataMap(entityMetadata);

        entityDataService.registerService('WorkingTime', workingTimeDataService);

    }
 }
