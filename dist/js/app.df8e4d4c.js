(function(t){function e(e){for(var n,o,s=e[0],l=e[1],c=e[2],d=0,v=[];d<s.length;d++)o=s[d],a[o]&&v.push(a[o][0]),a[o]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(t[n]=l[n]);u&&u(e);while(v.length)v.shift()();return r.push.apply(r,c||[]),i()}function i(){for(var t,e=0;e<r.length;e++){for(var i=r[e],n=!0,s=1;s<i.length;s++){var l=i[s];0!==a[l]&&(n=!1)}n&&(r.splice(e--,1),t=o(o.s=i[0]))}return t}var n={},a={app:0},r=[];function o(e){if(n[e])return n[e].exports;var i=n[e]={i:e,l:!1,exports:{}};return t[e].call(i.exports,i,i.exports,o),i.l=!0,i.exports}o.m=t,o.c=n,o.d=function(t,e,i){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:i})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var i=Object.create(null);if(o.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)o.d(i,n,function(e){return t[e]}.bind(null,n));return i},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=e,s=s.slice();for(var c=0;c<s.length;c++)e(s[c]);var u=l;r.push([0,"chunk-vendors"]),i()})({0:function(t,e,i){t.exports=i("56d7")},1:function(t,e){},"56d7":function(t,e,i){"use strict";i.r(e);i("cadf"),i("551c"),i("097d");var n=i("2b0e"),a=i("28dd"),r=i("bb71");i("da64");n["a"].use(r["a"],{iconfont:"md"});var o=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-app",[i("v-layout",{attrs:{row:""}},[i("v-toolbar",{attrs:{color:"blue darken-3",dark:"",app:"",fixed:""}},[i("v-toolbar-side-icon"),i("v-toolbar-title",{staticClass:"ml-0 pl-3",staticStyle:{width:"300px"}},[i("span",{staticClass:"hidden-sm-and-down"},[t._v("Система учёта персонала")])]),i("v-spacer"),i("v-spacer"),i("v-btn",{attrs:{icon:""}},[i("v-icon",[t._v("notifications_none")])],1),i("MenuFilter"),i("v-btn",{attrs:{icon:"",href:"https://github.com/andribas404/shell",target:"_blank"}},[i("img",{attrs:{height:"32",width:"32",src:"/github.svg"}})])],1),i("v-content",[i("PersonsList")],1)],1)],1)},s=[],l=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-container",{attrs:{fluid:"","fill-height":""}},[i("v-layout",{attrs:{"align-center":"","justify-center":""}},[t.items.length?i("v-list",{attrs:{"two-line":""}},t._l(t.items,function(e){return i("ListItem",{key:e.id,attrs:{item:e},on:{edit:t.editItem,archive:t.archiveToggleItem}})}),1):i("p",[t._v("\n      Список сотрудников пуст.\n    ")]),i("v-btn",{attrs:{color:"red",dark:"",fab:"",bottom:"",left:"",fixed:""},on:{click:function(e){t.$vuetify.goTo(0,{duration:500,offset:0})}}},[i("v-icon",[t._v("keyboard_arrow_up")])],1),i("v-btn",{attrs:{color:"pink",dark:"",fab:"",bottom:"",right:"",fixed:""},on:{click:t.addItem}},[i("v-icon",[t._v("add")])],1),i("PersonForm",{ref:"add_form",on:{create:t.createItem,update:t.updateItem}}),i("PersonForm",{ref:"edit_form",attrs:{edit_mode:""},on:{create:t.createItem,update:t.updateItem,remove:t.removeItem}}),i("Notice",{ref:"snack"})],1)],1)},c=[],u=(i("20d6"),i("28a5"),i("a4bb")),d=i.n(u),v=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-list-tile",{attrs:{avatar:""},on:{click:function(e){t.$emit("edit",t.item.id)}}},[i("v-list-tile-avatar",[i("v-icon",{class:[t.item.iconClass]},[t._v(t._s(t.item.icon))])],1),i("v-list-tile-content",[i("v-list-tile-title",[t._v(t._s(t.item.title))]),i("v-list-tile-sub-title",[t._v(t._s(t.item.subtitle))])],1),i("v-list-tile-action",[i("v-btn",{attrs:{icon:""},on:{click:function(e){e.stopPropagation(),t.$emit("archive",t.item.id)}}},[t.item.is_archive?i("v-icon",{attrs:{color:"grey lighten-1"}},[t._v("\n            star_border\n            ")]):i("v-icon",{attrs:{color:"yellow darken-2"}},[t._v("\n            star\n            ")])],1)],1)],1)},f=[],m={props:{item:{type:Object,required:!0}}},p=m,h=i("2877"),b=i("6544"),_=i.n(b),g=i("8336"),x=i("132d"),k=i("ba95"),y=i("40fe"),V=i("c954"),w=i("5d23"),$=Object(h["a"])(p,v,f,!1,null,null,null);$.options.__file="ListItem.vue";var I=$.exports;_()($,{VBtn:g["a"],VIcon:x["a"],VListTile:k["a"],VListTileAction:y["a"],VListTileAvatar:V["a"],VListTileContent:w["a"],VListTileSubTitle:w["b"],VListTileTitle:w["c"]});var T=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-dialog",{attrs:{fullscreen:"","hide-overlay":"",transition:"dialog-bottom-transition"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[i("v-card",[t.edit_mode?i("v-toolbar",{attrs:{dark:"",color:"blue darken-3"}},[i("v-btn",{attrs:{icon:"",dark:""},on:{click:t.close}},[i("v-icon",[t._v("close")])],1),i("v-toolbar-title",[t._v("Редактирование сотрудника")]),i("v-spacer"),i("v-toolbar-items",[i("v-btn",{attrs:{dark:"",flat:""},on:{click:function(e){t.$emit("update",t.item)}}},[t._v("Сохранить")])],1)],1):i("v-toolbar",{attrs:{dark:"",color:"blue darken-3"}},[i("v-btn",{attrs:{icon:"",dark:""},on:{click:t.close}},[i("v-icon",[t._v("close")])],1),i("v-toolbar-title",[t._v("Добавление сотрудника")]),i("v-spacer"),i("v-toolbar-items",[i("v-btn",{attrs:{dark:"",flat:""},on:{click:function(e){t.$emit("create",t.item)}}},[t._v("Создать")])],1)],1),i("v-form",{model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[i("v-container",{attrs:{"grid-list-md":"","text-xs-center":""}},[i("v-layout",{attrs:{row:"",wrap:""}},[i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-text-field",{attrs:{rules:t.fieldRules,label:"Имя",required:""},model:{value:t.item.first_name,callback:function(e){t.$set(t.item,"first_name",e)},expression:"item.first_name"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-text-field",{attrs:{rules:t.fieldRules,label:"Отчество",required:""},model:{value:t.item.second_name,callback:function(e){t.$set(t.item,"second_name",e)},expression:"item.second_name"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-text-field",{attrs:{rules:t.fieldRules,label:"Фамилия",required:""},model:{value:t.item.last_name,callback:function(e){t.$set(t.item,"last_name",e)},expression:"item.last_name"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-select",{attrs:{items:t.sex_items,rules:t.fieldRules,label:"Пол",required:""},model:{value:t.item.sex,callback:function(e){t.$set(t.item,"sex",e)},expression:"item.sex"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-text-field",{attrs:{rules:t.fieldRules,label:"Дата рождения",required:""},model:{value:t.item.birthday,callback:function(e){t.$set(t.item,"birthday",e)},expression:"item.birthday"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-select",{attrs:{items:t.dpt_items,rules:t.fieldRules,label:"Отдел",required:""},model:{value:t.item.dpt,callback:function(e){t.$set(t.item,"dpt",e)},expression:"item.dpt"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-text-field",{attrs:{rules:t.fieldRules,label:"Должность",required:""},model:{value:t.item.position,callback:function(e){t.$set(t.item,"position",e)},expression:"item.position"}})],1),i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-checkbox",{attrs:{label:"В архиве"},model:{value:t.item.is_archive,callback:function(e){t.$set(t.item,"is_archive",e)},expression:"item.is_archive"}})],1),t.edit_mode?i("v-flex",{attrs:{xs12:"",md4:""}},[i("v-btn",{attrs:{dark:"",color:"red"},on:{click:t.confirm}},[i("v-icon",[t._v("delete")]),t._v(" Удалить\n                ")],1)],1):t._e()],1)],1)],1)],1),i("Confirmation",{ref:"confirm",attrs:{dialog:t.confirm_dialog},on:{confirm:t.confirmed}})],1)},j=[],C=(i("7f7f"),function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-layout",{attrs:{row:"","justify-center":""}},[i("v-dialog",{attrs:{persistent:"","max-width":"290"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[i("v-card",[i("v-card-title",{staticClass:"headline"},[t._v("\n        Подтверждение\n      ")]),i("v-card-text",[t._v(t._s(t.text))]),i("v-card-actions",[i("v-spacer"),i("v-btn",{attrs:{color:"green darken-1",flat:""},on:{click:function(e){t.dialog=!1}}},[t._v("\n          Отмена\n        ")]),i("v-btn",{attrs:{color:"green darken-1",flat:""},on:{click:function(e){t.$emit("confirm")}}},[t._v("\n          Удалить\n        ")])],1)],1)],1)],1)}),N=[],L={data:function(){return{dialog:!1,confirmed:!1,text:"Вы точно хотите удалить сотрудника?"}},methods:{show:function(){var t=!(arguments.length>0&&void 0!==arguments[0])||arguments[0];this.dialog=t}}},O=L,F=i("b0af"),P=i("99d9"),S=i("12b2"),R=i("169a"),q=i("a722"),B=i("9910"),D=Object(h["a"])(O,C,N,!1,null,null,null);D.options.__file="Confirmation.vue";var M=D.exports;_()(D,{VBtn:g["a"],VCard:F["a"],VCardActions:P["a"],VCardText:P["b"],VCardTitle:S["a"],VDialog:R["a"],VLayout:q["a"],VSpacer:B["a"]});var A={components:{Confirmation:M},props:{edit_mode:{type:Boolean}},data:function(){return{confirm_dialog:!1,dialog:!1,valid:!1,item:{first_name:"",second_name:"",last_name:"",sex:null,birthday:"",dpt:null,position:"",is_archive:!1},fieldRules:[function(t){return!!t||"Обязательное поле"}],sex_items:[{text:"Мужской",value:"М"},{text:"Женский",value:"Ж"}],dpt_items:[]}},methods:{set:function(t){var e=this,i="person/"+t;this.$http.get(i).then(function(t){var i=t.body;e.item=i,e.item.dpt=i.dpt.id,e.item.birthday=i.birthday.split("-").reverse().join(".")},function(t){})},show:function(){var t=!(arguments.length>0&&void 0!==arguments[0])||arguments[0];this.dialog=t},close:function(){this.dialog=!1},confirm:function(){this.$refs.confirm.show()},confirmed:function(){this.$refs.confirm.show(!1),this.$emit("remove",this.item)}},created:function(){var t=this;this.$http.get("dpt").then(function(e){for(var i=e.body,n=[],a=i.length,r=0;r<a;r++)n.push({text:i[r].name,value:i[r].id});t.dpt_items=n},function(t){})}},E=A,J=i("ac7c"),G=i("a523"),z=i("0e8f"),H=i("4bd4"),K=i("b56d"),Q=i("2677"),U=i("71d9"),W=i("2a7f"),X=Object(h["a"])(E,T,j,!1,null,null,null);X.options.__file="PersonForm.vue";var Y=X.exports;_()(X,{VBtn:g["a"],VCard:F["a"],VCheckbox:J["a"],VContainer:G["a"],VDialog:R["a"],VFlex:z["a"],VForm:H["a"],VIcon:x["a"],VLayout:q["a"],VSelect:K["a"],VSpacer:B["a"],VTextField:Q["a"],VToolbar:U["a"],VToolbarItems:W["a"],VToolbarTitle:W["b"]});var Z=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-snackbar",{attrs:{top:"","multi-line":"",timeout:3e3},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n  "+t._s(t.text)+"\n  "),i("v-btn",{attrs:{color:"pink",flat:""},on:{click:function(e){t.snackbar=!1}}},[t._v("\n    Закрыть\n  ")])],1)},tt=[],et={data:function(){return{snackbar:!1,text:"",status:""}},methods:{show:function(t,e){this.status=t,this.text=e,this.snackbar=!0}}},it=et,nt=i("2db4"),at=Object(h["a"])(it,Z,tt,!1,null,null,null);at.options.__file="Notice.vue";var rt=at.exports;_()(at,{VBtn:g["a"],VSnackbar:nt["a"]});var ot={components:{ListItem:I,PersonForm:Y,Notice:rt},data:function(){return{items:[]}},methods:{addItem:function(){this.$refs.add_form.show()},editItem:function(t){this.$refs.edit_form.set(t),this.$refs.edit_form.show()},getFormData:function(t){for(var e=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],i=new FormData,n=d()(t),a=0;a<n.length;a++){var r=n[a],o=t[r];e&"birthday"===r&&(o=o.split(".").reverse().join("-")),i.append(r,o)}return i},removeItem:function(t){var e=this,i="person/"+t.id+"/delete",n=this.getFormData({id:t.id}),a=this.getName(t);this.$http.post(i,n).then(function(i){var n="Сотрудник "+a+" удален";e.$refs.edit_form.show(!1),e.popItem(t),e.showNotice("success",n)},function(t){var i="Ошибка сохранения сотрудника "+a+". Причина: "+t.body.message;e.showNotice("error",i)})},archiveToggleItem:function(t){var e=this,i="person/"+t;this.$http.get(i).then(function(t){var i=t.body;i.dpt=i.dpt.id,i.is_archive=!i.is_archive,e.archivePostItem(i)},function(t){e.showNotice("error","error loading data from api"+t.status)})},archivePostItem:function(t){var e=this,i="person/"+t.id,n="из архива";t.is_archive&&(n="в архив");var a=this.getFormData(t,!1);this.$http.post(i,a).then(function(i){var a="Сотрудник "+name+" перемещен "+n;e.showNotice("success",a);var r=e.items.findIndex(function(e){return e.id===t.id});-1===r||e.$set(e.items,r,e.transformItem(t))},function(t){var i="Ошибка перемещения сотрудника "+name+" "+n+". Причина: "+t.body.message;e.showNotice("error",i)})},createItem:function(t){var e=this,i=this.getFormData(t),n="person";this.$http.post(n,i).then(function(t){var i=t.body,n=e.getName(i),a="Сотрудник "+n+" успешно создан";e.$refs.add_form.show(!1),e.appendItem(i),e.showNotice("success",a)},function(t){var i="Ошибка создания сотрудника "+name+". Причина: "+t.body.message;e.showNotice("error",i)})},updateItem:function(t){var e=this,i="person/"+t.id,n=this.getFormData(t),a=this.getName(t);this.$http.post(i,n).then(function(i){var n="Сотрудник "+a+" успешно сохранен";e.$refs.edit_form.show(!1),e.refreshItem(t),e.showNotice("success",n)},function(t){var i="Ошибка сохранения сотрудника "+a+". Причина: "+t.body.message;e.showNotice("error",i)})},getName:function(t){return[t.first_name,t.second_name,t.last_name].join(" ")},transformItem:function(t){var e=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],i=this.getName(t),n=t.birthday;e&&(n=n.split("-").reverse().join("."));var a=["Дата рождения:",n].join(" ");return{icon:"person",iconClass:"blue white--text",title:i,subtitle:a,is_archive:t.is_archive,id:t.id}},showNotice:function(t,e){this.$refs.snack.show(t,e)},refreshItem:function(t){var e=this.items.findIndex(function(e){return e.id===t.id});-1===e||this.$set(this.items,e,this.transformItem(t,!1))},appendItem:function(t){var e=this.transformItem(t,!1);this.items.push(e)},popItem:function(t){var e=this.items.findIndex(function(e){return e.id===t.id});-1===e||this.items.splice(e,1)}},created:function(){var t=this;this.$http.get("person").then(function(e){for(var i=e.body,n=[],a=i.length,r=0;r<a;r++){var o=i[r],s=t.transformItem(o);n.push(s)}t.items=n},function(e){t.showNotice("error","error loading data from api"+e.status)})}},st=ot,lt=i("8860"),ct=Object(h["a"])(st,l,c,!1,null,null,null);ct.options.__file="PersonsList.vue";var ut=ct.exports;_()(ct,{VBtn:g["a"],VContainer:G["a"],VIcon:x["a"],VLayout:q["a"],VList:lt["a"]});var dt=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-menu",{attrs:{"close-on-content-click":!1,"offset-y":""},model:{value:t.menu,callback:function(e){t.menu=e},expression:"menu"}},[i("v-btn",{attrs:{slot:"activator",icon:""},slot:"activator"},[i("v-icon",[t._v("widgets")])],1),i("v-card",[i("v-card-title",{attrs:{"primary-title":""}},[i("v-layout",{attrs:{column:""}},[i("h3",[t._v("Фильтр")]),i("v-radio-group",{model:{value:t.choice,callback:function(e){t.choice=e},expression:"choice"}},[i("v-radio",{key:0,attrs:{label:"Только активные",value:0}}),i("v-radio",{key:1,attrs:{label:"Только архив",value:1}}),i("v-radio",{key:2,attrs:{label:"Все",value:2}})],1)],1)],1),i("v-card-actions",[i("v-spacer"),i("v-btn",{attrs:{flat:""},on:{click:function(e){t.menu=!1}}},[t._v("\n        Отмена\n      ")]),i("v-btn",{attrs:{color:"primary",flat:""},on:{click:function(e){t.menu=!1}}},[t._v("\n        Применить\n      ")])],1)],1)],1)},vt=[],ft={data:function(){return{menu:!1,choice:1}}},mt=ft,pt=i("e449"),ht=i("67b6"),bt=i("43a6"),_t=Object(h["a"])(mt,dt,vt,!1,null,null,null);_t.options.__file="MenuFilter.vue";var gt=_t.exports;_()(_t,{VBtn:g["a"],VCard:F["a"],VCardActions:P["a"],VCardTitle:S["a"],VIcon:x["a"],VLayout:q["a"],VMenu:pt["a"],VRadio:ht["a"],VRadioGroup:bt["a"],VSpacer:B["a"]});var xt={name:"App",components:{PersonsList:ut,MenuFilter:gt},data:function(){return{}}},kt=xt,yt=i("7496"),Vt=i("549c"),wt=i("706c"),$t=Object(h["a"])(kt,o,s,!1,null,null,null);$t.options.__file="App.vue";var It=$t.exports;_()($t,{VApp:yt["a"],VBtn:g["a"],VContent:Vt["a"],VIcon:x["a"],VLayout:q["a"],VSpacer:B["a"],VToolbar:U["a"],VToolbarSideIcon:wt["a"],VToolbarTitle:W["b"]});var Tt="";Tt="https://person-list.herokuapp.com/api";var jt=Tt;n["a"].use(a["a"]),n["a"].http.options.root=jt,n["a"].config.productionTip=!1,new n["a"]({render:function(t){return t(It)}}).$mount("#app")}});
//# sourceMappingURL=app.df8e4d4c.js.map