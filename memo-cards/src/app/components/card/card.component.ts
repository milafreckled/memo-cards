import { animate, state, style, transition, trigger, useAnimation } from '@angular/animations';
import { Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { Navigation, NavigationStart, Router } from '@angular/router';

import { DbServiceService, ITerm } from "../../services/db-service.service"
import { reusableAnimation } from './reusableAnimation';
@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
  animations: [
    trigger('searchTrigger', [
      state('empty', style({
        backgroundImage: "url('../../../assets/svg/search-icon.svg')",
        backgroundSize: '16px 16px'
      })),
      state('searching', style({
        backgroundImage: 'none',      
        backgroundSize: '0 0'
      })),
      transition('empty <=> searching', animate('0.5s ease-in-out'))
    ])
  ]
})
export class CardComponent{
  listenForSearch!: () => void;
  @ViewChild("searchInputEl", {static: true}) 
  searchInputRef!: ElementRef;
  searchValue = '';
  difficultyLevel: string = "easy";
  constructor(private dbService: DbServiceService,  private router: Router, private renderer2: Renderer2){};
  editMode = false;
  editTerm!: ITerm;
  cards: ITerm[] = [];
  ngOnInit(): void{
    this.listenForSearch = this.renderer2.listen(this.searchInputRef.nativeElement, 'keydown', (e) => {
      // console.log('Search value: ', this.searchValue);
      if (e.keyCode === 13){
        this.dbService.getTermBySearch(this.searchValue)
        .subscribe(filtered => {
          this.cards = filtered as unknown as ITerm[];
        });
      }
    });
    this.dbService.getTerms().subscribe(terms => this.cards = terms);
  };
  onDelete(term: string){
    this.dbService.deleteTerm(term).subscribe(() => this.cards = this.cards.filter(c => c.term !== term));
  };
  onEdit(termObj: ITerm){
    this.editMode = true;
    this.editTerm = termObj;
  };
  onChangeDifficultyLevel(data: string){
    console.log(`Data: ${data}`)
    this.difficultyLevel = data;
  }
  ngOnDestroy(){
    this.listenForSearch();
  };
}
