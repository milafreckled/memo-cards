import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthConfig, OAuthService } from 'angular-oauth2-oidc';
import { catchError, Subject } from 'rxjs';

export interface UserInfo {
  info: {
    sub: string;
    name: string;
    email: string;
    picture: string;
  }
}

const oAuthConfig: AuthConfig = {
  issuer: 'https://accounts.google.com',
  strictDiscoveryDocumentValidation: false,
  redirectUri: window.location.origin + '/practice',
  clientId: '107803128621-56g82g6mg890oha7jl0i0sno17lvk5e7.apps.googleusercontent.com',
  requestAccessToken: true,
  showDebugInformation: true,
  dummyClientSecret: 'secret',
  scope: 'openid profile email'
};

@Injectable({
  providedIn: 'root'
})

export class GoogleApiService {
  userProfileSubject = new Subject<UserInfo>();
  loggedIn = false;
  loggedInByEmail = false;
  constructor(private readonly oAuthService: OAuthService, private http: HttpClient) {
    oAuthService.configure(oAuthConfig);
    oAuthService.loginUrl = "https://www.google.com/accounts/Logout";
    // oAuthService.loadDiscoveryDocument().then(() => {
    //   oAuthService.tryLoginImplicitFlow().then(() => {
    //     if (!oAuthService.hasValidAccessToken()){
    //       oAuthService.initLoginFlow();
    //       this.loggedIn = true;
    //     }else{
    //       oAuthService.loadUserProfile().then((userProfile) => {
    //         this.userProfileSubject.next(userProfile as UserInfo);
    //       })
    //     }
    //   });
    // })
   };
   isLoggedIn(): boolean{
    console.log('Checking for valid token');
    return this.oAuthService.hasValidAccessToken();
   };
   signOut(){
    this.oAuthService.logOut();
   }
   // login with magic link
   login(email: string, name: string){
      this.loggedInByEmail = true;
      return this.http.post('/api/login', { email, name }, { headers: new HttpHeaders({'content-type': 'application/json'})}).pipe(catchError(
        async (err) => {
          this.loggedInByEmail = false;
          console.error(err)
      }));
   }
}
