import { AfterViewChecked, ChangeDetectionStrategy, Component, ElementRef, NgZone, OnInit, Renderer2, ViewChild, ViewContainerRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TimeProcessComponent } from "../time-process/time-process.component";

declare const $: any;

@Component({
    selector: 'app-time-card',
    standalone: true,
    templateUrl: './time-card.component.html',
    styleUrls: ['./time-card.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
    imports: [CommonModule, TimeProcessComponent]
})
export class TimeCardComponent implements OnInit {
  @ViewChild('template', { static: true }) template;
  
  constructor(private el: ElementRef, private renderer: Renderer2, private ngZone: NgZone, private viewContainerRef: ViewContainerRef) {}

  ngOnInit(): void {
    let a = this.viewContainerRef.createEmbeddedView(this.template);
  }
}
