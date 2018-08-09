<template>
<v-app id="app">
      <v-navigation-drawer
      v-model="drawer"
      fixed
      clipped
      class="grey lighten-4"
      app
    >
      <v-list
        dense
        class="grey lighten-4"
      >
        <template v-for="(item, i) in navInfo">
          <v-layout
            v-if="item.heading"
            :key="i"
            row
            align-center
          >
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
          </v-layout>
          <v-divider
            v-else-if="item.divider"
            :key="i"
            dark
            class="my-3"
          ></v-divider>
          <v-list-tile
            v-else
            :key="i"
            @click="tab = item.tab; indicatorSelected = item.indicator"
          >
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title class="grey--text">
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar class="blue-grey" style="color:white;" app fixed clipped-left>
      <v-toolbar-side-icon style="color:white;" @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Crypto Signals</v-toolbar-title>
    </v-toolbar>
    <v-content v-show="tab === 'RSI'">
      <h1>RSI</h1>
      <v-container fluid>
        <v-layout>
          <v-flex>
            <v-layout justify-center >
              <template v-for="item in items">
                <v-btn class="blue-grey" style="color: white;" v-bind:key="item" :value="item.name" @click="row = item">{{ item.name }}</v-btn>
              </template>
            </v-layout>
            <v-layout child-flex row>
              <v-data-table v-bind:headers="mainHeaders"
                :items="row.data"
                hide-actions>
                <template slot="items" slot-scope="props">
                  <tr>
                    <td class="text-xs">{{props.item.coin}}</td>
                    <td class="text-xs">{{props.item.status}}</td>
                    <td class="text-xs"> {{props.item.RSI_Level}}</td>
                  </tr>
                </template>
              </v-data-table>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-content v-show="tab === 'EMA'">
      <h1>EMA</h1>
      <v-container fluid>
        <v-layout>
          <v-flex>
            <v-layout justify-center >
              <template v-for="item in items">
                <v-btn class="blue-grey" style="color: white;" v-bind:key="item" :value="item.name" @click="row = item">{{ item.name }}</v-btn>
              </template>
            </v-layout>
            <v-layout>
              <v-data-table v-bind:headers="mainHeaders"
                :items="row.data"
                hide-actions>
                <template slot="items" slot-scope="props">
                  <tr>
                    <td class="text-xs">{{props.item.coin}}</td>
                    <td class="text-xs">{{props.item.status}}</td>
                  </tr>
                </template>
              </v-data-table>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-content v-show="tab === 'about'">
      <v-container style="padding-top: 0px;" fluid>
        <v-layout>
          <v-flex xs6>
            <img src="/static/IMG_0743.png" alt="Me" style="width: 100%;">
          </v-flex>
          <v-flex xs1>
          </v-flex>
          <v-flex xs4 style="padding-top: 3em;">
            <h1>About Me</h1>
            <p>Hey what's up? My name's Connor and I currently live in Philly. My full time gig is a Mechanical Engineer but I love to code on the side. I really enjoy building web apps (both front and backend). Other than that I love to go to the beach and spending time outdoors. If you have any questions or comments please let me know and I promise I will answer you! Thanks! Hope this tool helps you identify possible trades!</p>
            <v-layout row>
              <v-flex xs3>
                <a class="icon" href="https://www.instagram.com/connor_hill22/" style="text-decoration:none;"><v-icon size="3em">fa fa-instagram</v-icon></a>
              </v-flex>
              <v-flex xs2>
              </v-flex>
              <v-flex xs3>
                <a class="icon" href="https://www.facebook.com/chill0594" style="text-decoration:none;"><v-icon size="3em">fa-facebook-square</v-icon></a>
              </v-flex>
              <v-flex xs2>
              </v-flex>
              <v-flex xs3>
                <a class="icon" href="https://www.linkedin.com/in/connor-hill-9771537a" style="text-decoration:none;"><v-icon size="3em">fa-linkedin</v-icon></a>
              </v-flex>
            </v-layout>
          </v-flex>
          <v-flex xs1>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  <v-footer app fixed justify-center>
    <v-flex xs12 py-3 text-xs-center>
      Created by: <strong>Connor Hill</strong><a class="icon" href="https://www.instagram.com/connor_hill22/" style="padding-left:0.75em; text-decoration:none;"><v-icon size="0.75em">fa fa-instagram</v-icon></a>
      <a class="icon" href="https://www.linkedin.com/in/connor-hill-9771537a" style="padding-left:0.75em; text-decoration:none;"><v-icon size="0.75em">fa-linkedin</v-icon></a>
      <a class="icon" href="https://www.facebook.com/chill0594" style="padding-left:0.75em; text-decoration:none;"><v-icon size="0.75em">fa-facebook-square</v-icon></a>
    </v-flex>
  </v-footer>
</v-app>
</template>

<script>
import axios from 'axios'

let baseUrl = 'http://127.0.0.1:5000/api/'

export default {
  name: 'signals',
  el: '#app',

  data: () => ({
    navInfo: [
      { icon: 'lightbulb_outline', text: 'Home', tab: 'home' },
      { divider: true },
      { heading: 'Signals' },
      { icon: '', text: 'RSI', tab: 'RSI', indicator: 'RSIstore' },
      { icon: '', text: 'SMA', tab: 'SMA' },
      { icon: '', text: 'EMA', tab: 'EMA', indicator: 'EMAstore' },
      { divider: true },
      { icon: 'archive', text: 'About', tab: 'about' },
      { icon: 'delete', text: 'Help', tab: 'help' },
      { icon: 'delete', text: 'Disclaimer', tab: 'disclaimer' }],
    page: ['home', 'about'],
    mainHeaders: [{ text: 'Coin', value: 'coin' },
      { text: 'Status', value: 'status' },
      { text: 'RSI Level', value: 'RSI_Level' }],
    intervals: ['5 Minute', '15 Minute', '1 Hour', '4 Hour', '1 Day'],
    items: [
      {
        name: '5 Minute',
        data: {}
      },
      {
        name: '15 Minute',
        data: {}
      },
      {
        name: '1 Hour',
        data: {}
      },
      {
        name: '4 Hour',
        data: {}
      },
      {
        name: '1 Day',
        data: {}
      }
    ],
    errors: [],
    current_time: '',
    indicatorSelected: '',
    currentTab: '',
    tab: 'home',
    row: []
  }),

  watch: {
    tab: function (val) {
      this.loadInitialData()
    }
  },

  beforeDestroy () {
    clearInterval(this.intervalid1)
  },
  methods: {
    loadInitialData: function () {
      axios.get(baseUrl + '5m/' + this.indicatorSelected)
        .then(response => {
          this.items[0].data = response.data
          console.log(this.items)
          var currentdate = new Date()
          this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
        })
      axios.get(baseUrl + '15m/' + this.indicatorSelected)
        .then(response => {
          this.items[1].data = response.data
          var currentdate = new Date()
          this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
        })
      axios.get(baseUrl + '1h/' + this.indicatorSelected)
        .then(response => {
          this.items[2].data = response.data
          var currentdate = new Date()
          this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
        })
      axios.get(baseUrl + '4h/' + this.indicatorSelected)
        .then(response => {
          this.items[3].data = response.data
          var currentdate = new Date()
          this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
        })
      axios.get(baseUrl + '1d/' + this.indicatorSelected)
        .then(response => {
          this.items[4].data = response.data
          var currentdate = new Date()
          this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
        })
      this.loadData()
    },
    loadData: function () {
      this.intervalid1 = setInterval(function () {
        axios.get(baseUrl + '5m/' + this.indicatorSelected)
          .then(response => {
            this.items[0].data = response.data
            console.log(this.items)
            var currentdate = new Date()
            this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
          })
        axios.get(baseUrl + '15m/' + this.indicatorSelected)
          .then(response => {
            this.items[1].data = response.data
            var currentdate = new Date()
            this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
          })
        axios.get(baseUrl + '1h/' + this.indicatorSelected)
          .then(response => {
            this.items[2].data = response.data
            var currentdate = new Date()
            this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
          })
        axios.get(baseUrl + '4h/' + this.indicatorSelected)
          .then(response => {
            this.items[3].data = response.data
            var currentdate = new Date()
            this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
          })
        axios.get(baseUrl + '1d/' + this.indicatorSelected)
          .then(response => {
            this.items[4].data = response.data
            var currentdate = new Date()
            this.current_time = 'Last Updated: ' + currentdate.getDate() + '/' + (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' @ ' + currentdate.getHours() + ':' + currentdate.getMinutes() + ':' + currentdate.getSeconds() + 'UTC'
          })
      }.bind(this), 60000)
    }
  }
}
</script>

<style>
.img{
  max-width: 50%;
}
.table th {
  text-align: center;
  font-size: large;
}
.icon:hover{
  color: rgb(238, 62, 62);
}
</style>
