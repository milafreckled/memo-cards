import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Route, Router, NavigationStart } from '@angular/router';
import { PracticeComponent } from './components/practice/practice.component';
import { AddTermComponent } from './components/add-term/add-term.component';
import { CardComponent } from './components/card/card.component';
import { filter } from 'rxjs/operators';
import { AuthGuardGuard } from './guards/auth-guard.guard';
import { LoginComponent } from './components/login/login.component';
import { NotFoundComponent } from './components/not-found/not-found.component';

const routes: Route[] = [
{ path: 'practice', canActivate: [AuthGuardGuard],  component: PracticeComponent }, 
{ path: '', redirectTo: 'practice', pathMatch: 'full' }, 
{ path: 'newTerm', component: AddTermComponent },
{ path: 'terms', component: CardComponent },
{ path: 'login', component: LoginComponent },
{ path: '**', component: NotFoundComponent}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {
  constructor(private router: Router){
  this.router.events.pipe(filter(e => e instanceof NavigationStart)).subscribe(e => {
    const navigation = this.router.getCurrentNavigation();
    console.info('Current navigation:', navigation)
  })
}
}
