import { EntityMetadataMap } from "@ngrx/data";

export const entityMetadata: EntityMetadataMap = {
    WorkingTime: {
        entityDispatcherOptions: {
            optimisticUpdate: true
        }
    }
};
