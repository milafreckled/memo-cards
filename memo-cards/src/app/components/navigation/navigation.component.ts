import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { filter } from 'rxjs';
import { DbServiceService, ITerm } from '../../services/db-service.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  terms!: ITerm[];
  constructor(private form: FormBuilder, private dbService: DbServiceService, private router: Router){}
  addNewTerm = false;
  ngOnInit(){
    this.dbService.getTerms().subscribe(terms => this.terms = terms);
  };
}
