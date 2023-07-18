import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WorkingTimeResolver } from './services/working-time.resolver';
import { WorkingTimeComponent } from './working-time/working-time.component';

const routes: Routes = [
  {
    path: 'working-time',        
    component: WorkingTimeComponent,
    resolve: {
      workingTimes: WorkingTimeResolver
    }
  },
  {
    path: '',
    component: WorkingTimeComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReportsRoutingModule { }
