import { NgModule, isDevMode } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { CardComponent } from './components/card/card.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { DbServiceService } from "./services/db-service.service"
import { RouterModule } from '@angular/router';
import { AddTermComponent } from './components/add-term/add-term.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { PracticeComponent } from './components/practice/practice.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { AppRoutingModule } from './app-routing.module';
import { NbThemeModule, NbSearchModule, NbLayoutModule } from '@nebular/theme'
import { NotFoundComponent } from './components/not-found/not-found.component';
import { LoginComponent } from './components/login/login.component';
import { OAuthModule } from 'angular-oauth2-oidc';
import { DifficultyChooserComponent } from './components/difficulty-chooser/difficulty-chooser.component';
import { GoogleApiService } from './services/google-api.service';

@NgModule({
    declarations: [
        AppComponent,
        CardComponent,
        NavigationComponent,
        AddTermComponent,
        PracticeComponent,
        LoginComponent,
        NotFoundComponent,
        DifficultyChooserComponent
    ],
    providers: [
        DbServiceService,
        GoogleApiService
    ],
    bootstrap: [AppComponent],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        ReactiveFormsModule,
        ServiceWorkerModule.register('ngsw-worker.js', {
          enabled: !isDevMode(),
          // Register the ServiceWorker as soon as the application is stable
          // or after 30 seconds (whichever comes first).
          registrationStrategy: 'registerWhenStable:30000'
        }),
        FormsModule,
        ReactiveFormsModule,
        AppRoutingModule,
        OAuthModule.forRoot(),
        NbThemeModule.forRoot(),
        NbSearchModule,
        NbLayoutModule,
    ],
    exports: [
        RouterModule
    ]
})
export class AppModule { }
