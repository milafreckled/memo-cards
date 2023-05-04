import { Component, ElementRef, Renderer2 } from '@angular/core';
import { DbServiceService, ITerm } from '../../services/db-service.service';

@Component({
  selector: 'app-practice',
  templateUrl: './practice.component.html',
  styleUrls: ['./practice.component.css']
})
export class PracticeComponent {
  constructor(private dbService: DbServiceService, private renderer2: Renderer2){};
  cardInnerRef!: ElementRef;
  timerNum = 0;
  timeOut = false;
  private unlistener!: () => void;
  allCards!: ITerm[];
  activeCard: ITerm = {
    term: '',
    definition: ''
  };
  canNavigate = true;
  
  getActiveCard(){
    return this.activeCard;
  };
  onMouseEnter(){
    this.canNavigate = false;
  };
  onMouseLeave(){
    this.canNavigate = true;
  };
  ngOnInit(): void{
    const timer = setInterval(() => {
        this.timerNum += 1;
        if (this.timerNum === 5){
          this.timeOut = true;
          document.getElementsByClassName('flip-card')[0].classList.add('rotate');
          clearInterval(timer);
        }
    }, 1000)
    this.unlistener = this.renderer2.listen("document", "keydown", event => {
      if (event.keyCode === 37 && this.canNavigate) this.getPrev();
      if (event.keyCode === 39 && this.canNavigate) this.getNext();
      const flipCardInner = this.cardInnerRef.nativeElement;
      flipCardInner.classList.remove('rotate');
    });
    this.dbService.getTerms().subscribe(terms => {
      this.allCards = this.shuffleCards(terms);
      this.activeCard = terms[0];
    });
  };
  // ngOnDestroy() {
  //   this.unlistener();
  // }
shuffleCards(arr: any[]): ITerm[] {
  let m = arr.length, t, i;
  while (m) {    
   i = Math.floor(Math.random() * m--);
   t = arr[m];
   arr[m] = arr[i];
   arr[i] = t;
  }
 return arr;
}
getPrev(){
  const currentIdx = this.allCards.indexOf(this.activeCard);
  this.activeCard = currentIdx !== 0 ? this.allCards[currentIdx - 1] : this.allCards[this.allCards.length - 1];
};
getNext(){
   const currentIdx = this.allCards.indexOf(this.activeCard);
   this.activeCard = currentIdx !== this.allCards.length - 1 ? this.allCards[currentIdx + 1] : this.allCards[0];
}
}
