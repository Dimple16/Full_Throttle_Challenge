import { Component, OnInit } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http, Headers, Jsonp } from '@angular/http';
import 'rxjs/add/operator/map';
@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  autocomplete:any;
  autoCompleteItems:Array<Object> = [];
  constructor(public navCtrl: NavController, public http:Http) {
  }

  ngOnInit(): void {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.
    this.autocomplete = {
      query: ''
    }
  }

  autoComplete()
  {
    this.http.get(`http://127.0.0.1:8080/searchString/getform?q=${this.autocomplete.query}`).map(res => res.json()).subscribe((res) => {
      console.log("check");
      // res.forEach(element => {
      //   this.autoCompleteItems.push(element);
      // });
      this.autoCompleteItems = res;
      console.log(this.autoCompleteItems);
    })
  }

  setSearchbarVal(data)
  {
    this.autocomplete.query = '';
    this.autocomplete.query = data;
  }

}
