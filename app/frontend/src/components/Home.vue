<template>
<v-app id="app">
    <v-toolbar class="blue-grey" style="color:white;" app fixed clipped-left>
      <v-toolbar-title>Crypto Signals</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid>
        <v-layout>
          <v-flex>
            <v-layout headline row >
              <h1>Welcome to Crypto Signals!</h1>
            </v-layout>
            <v-layout style="padding-top: 4em" row>
              <v-flex subheading style="text-align: left"><p>This little web app is pretty easy to understand, just follow the directions below. Feel free to reach out to me with any feedback or ideas! Currently I only have the RSI indicator however, there will be more indicators added in the future if people are interested! </p></v-flex>
              <v-flex sm4></v-flex>
            </v-layout>
            <v-layout style="padding-top: 1em">
              <v-flex headline style="text-align: left"><h3>Instructions:</h3></v-flex>
            </v-layout>
            <v-layout>
              <v-flex style="padding-top: 0.5em" subheading>
                <ul style="list-style-type: none">
                  <li style="text-align: left">1. Choose your indicator</li>
                  <li style="text-align: left">2. Choose your timeframe</li>
                  <li style="text-align: left">3. Scroll down to see all the signal!</li>
                </ul>
              </v-flex>
            </v-layout>
            <v-layout style="padding-top: 1em">
              <v-flex headline style="text-align: left"><h3>Some Notes</h3></v-flex>
            </v-layout>
            <v-layout>
              <v-flex style="padding-top: 0.5em; padding-left: 1em" subheading>
                <ul>
                  <li style="text-align: left">The page automatically updates every minute so no need to refresh the page!</li>
                  <li style="text-align: left">For lower volume coins the RSI may be off compared other websites</li>
                  <li style="text-align: left">I am NOT a financial advisor. This tool is in not a recommendation on what to buy or sell it is just a tool to help identify possible trades.</li>
                </ul>
              </v-flex>
            </v-layout>
            <v-layout row style="padding-top: 2em">
              <v-flex sm1></v-flex>
              <v-flex sm3>
                <v-flex title><h3>Select Indicator</h3></v-flex>
                <v-flex sm8 style="margin-left: 18%">
                  <v-select
                  :items="indicator"
                  item-text="name"
                  item-value="value"
                  placeholder="~Please Select~"
                  v-model="indicatorSelected"
                  ></v-select>
                </v-flex>
              </v-flex>
              <v-flex>
                <v-flex title><h3>Select Timeframe</h3></v-flex>
                <v-btn-toggle v-model="toggle">
                  <template v-for="item in items">
                    <v-btn class="blue-grey" style="color: white;" :disabled="item.disabled" v-bind:key="item" :value="item.name" @click="refreshFrontEnd(item)">{{ item.name }}</v-btn>
                  </template>
                </v-btn-toggle>
              </v-flex>
              <v-flex sm3>
                <v-flex title><h3>Last Updated (EST)</h3></v-flex>
                <h3 style="padding-top: 1em;">{{ current_time }}</h3>
              </v-flex>
              <v-flex sm1></v-flex>
            </v-layout>
            <v-layout child-flex row>
              <v-flex sm1></v-flex>
              <v-data-table v-bind:headers="mainHeaders"
                :items="stored[0].RSI_Triggers"
                hide-actions>
                <template slot="items" slot-scope="props">
                  <tr>
                    <td class="text-xs">{{props.item.coin}}</td>
                    <td class="text-xs">{{props.item.status}}</td>
                    <td class="text-xs"> {{props.item.RSI_Level}}</td>
                  </tr>
                </template>
              </v-data-table>
              <v-flex sm1></v-flex>
            </v-layout>
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
    mainHeaders: [
      { text: 'Coin', value: 'coin', align: 'center' },
      { text: 'Status', value: 'status', align: 'center' },
      { text: 'RSI Level', value: 'RSI_Level', align: 'center' }
    ],
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
    current_time: '',
    indicatorSelected: [],
    currentTab: '',
    indicator: [
      {
        name: 'RSI',
        value: 'RSIstore',
        disabled: ''
      },
      {
        name: 'VWAP',
        value: 'VWAP',
        disabled: 'true'
      }
    ],
    row: [],
    stored: [
      {
        RSI_Triggers: []
      }
    ],
    toggle: [],
    intervalid1: []
  }),

  watch: {
    indicatorSelected () {
      let self = this
      self.loadInitialData()
    }
  },

  beforeDestroy () {
    clearInterval(this.intervalid1)
  },
  methods: {
    refreshFrontEnd: function (item) {
      this.row = item
      this.current_time = this.row.data[0].time
      this.stored = this.row.data
      console.log('Ran1')
      setInterval(function () {
        var i
        for (i = 0; i < this.items.length; i++) {
          if (this.items[i].name === this.toggle) {
            this.row = this.items[i]
            this.current_time = this.row.data[0].time
            this.stored = this.row.data
            console.log(this.row.name)
          }
        }
      }.bind(this), 5000)
    },
    loadInitialData: function () {
      axios.get(baseUrl + '5m/' + this.indicatorSelected)
        .then(response => {
          this.items[0].data = response.data
        })
      axios.get(baseUrl + '15m/' + this.indicatorSelected)
        .then(response => {
          this.items[1].data = response.data
        })
      axios.get(baseUrl + '1h/' + this.indicatorSelected)
        .then(response => {
          this.items[2].data = response.data
        })
      axios.get(baseUrl + '4h/' + this.indicatorSelected)
        .then(response => {
          this.items[3].data = response.data
        })
      axios.get(baseUrl + '1d/' + this.indicatorSelected)
        .then(response => {
          this.items[4].data = response.data
        })
      this.loadData()
    },
    loadData: function () {
      this.intervalid1 = setInterval(function () {
        axios.get(baseUrl + '5m/' + this.indicatorSelected)
          .then(response => {
            this.items[0].data = response.data
            console.log(this.items)
          })
        axios.get(baseUrl + '15m/' + this.indicatorSelected)
          .then(response => {
            this.items[1].data = response.data
          })
        axios.get(baseUrl + '1h/' + this.indicatorSelected)
          .then(response => {
            this.items[2].data = response.data
          })
        axios.get(baseUrl + '4h/' + this.indicatorSelected)
          .then(response => {
            this.items[3].data = response.data
          })
        axios.get(baseUrl + '1d/' + this.indicatorSelected)
          .then(response => {
            this.items[4].data = response.data
          })
      }.bind(this), 5000)
    }
  }
}
</script>

<style>

.icon:hover{
  color: rgb(238, 62, 62);
}

</style>
