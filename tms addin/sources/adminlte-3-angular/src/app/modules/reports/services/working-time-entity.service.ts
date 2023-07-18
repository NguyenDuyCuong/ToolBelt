import { Injectable } from "@angular/core";
import { EntityCollectionServiceBase, EntityCollectionServiceElementsFactory } from "@ngrx/data";
import { WorkingTime } from "../models/working-time.model";

@Injectable()
export class WorkingTimeEntityService
    extends EntityCollectionServiceBase<WorkingTime> {

    constructor(
        serviceElementsFactory:
            EntityCollectionServiceElementsFactory) {

        super('WorkingTime', serviceElementsFactory);

    }

}