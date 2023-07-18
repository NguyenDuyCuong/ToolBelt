import { Injectable } from "@angular/core";
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot } from "@angular/router";
import { Observable, tap, filter, first } from "rxjs";
import { WorkingTimeEntityService } from "./working-time-entity.service";

@Injectable()
export class WorkingTimeResolver implements Resolve<boolean> {

    constructor(private workingTimeService: WorkingTimeEntityService) {

    }

    resolve(route: ActivatedRouteSnapshot,
            state: RouterStateSnapshot): Observable<boolean> {

        return this.workingTimeService.loaded$
            .pipe(
                tap(loaded => {
                    if (!loaded) {
                       this.workingTimeService.getAll();
                    }
                }),
                filter(loaded => !!loaded),
                first()
            );

    }

}