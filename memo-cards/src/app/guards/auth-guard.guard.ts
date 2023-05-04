import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';

import { GoogleApiService } from '../services/google-api.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardGuard implements CanActivate {
  constructor(private googleApi: GoogleApiService, private router: Router){};
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot):  boolean {
      let canActivate = true;
      setTimeout(() => {
      if (!this.googleApi.loggedInByEmail){
        this.router.navigate(['login']);
        canActivate = false;
      }
      }, 5000)
    return canActivate;
  }
  
}
