import { routerReducer } from "@ngrx/router-store";
import { ActionReducerMap, ActionReducer, MetaReducer } from "@ngrx/store";
import { environment } from "environments/environment";
import { authReducer } from "./auth/reducer";
import { AppState } from "./state";
import { uiReducer } from "./ui/reducer";

export const reducers: ActionReducerMap<AppState> = {
    router: routerReducer,
    auth: authReducer, 
    ui: uiReducer
};

export function logger(reducer:ActionReducer<any>)
    : ActionReducer<any> {
    return (state, action) => {
        console.log("state before: ", state);
        console.log("action", action);

        return reducer(state, action);
    }

}


export const metaReducers: MetaReducer<AppState>[] =
    !environment.production ? [logger] : [];