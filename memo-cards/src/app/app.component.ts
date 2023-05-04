import { Component, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor (private renderer2: Renderer2){}
  progressBar!: () => void;
  ngOnInit(){
    this.progressBar = this.renderer2.listen("document", "scroll", event => {
      const bar = document.getElementById('progress-bar');
      const scrollPosition = document.body.scrollTop || document.documentElement.scrollTop;
      let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      if (bar){
        bar.style.width = ((scrollPosition/height) * 100)+'%';
      }
    })
  }
};
