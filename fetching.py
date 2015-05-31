__author__ = 'Ankit_PC'
import urllib.request
import json
import re
from bs4 import BeautifulSoup
import pymongo

html="""
<!doctype html><!--[if lt IE 7]><html class="a-no-js a-lt-ie10 a-lt-ie9 a-lt-ie8 a-lt-ie7 a-ie6" data-19ax5a9jf="dingo"><![endif]--><!--[if IE 7]><html class="a-no-js a-lt-ie10 a-lt-ie9 a-lt-ie8 a-ie7" data-19ax5a9jf="dingo"><![endif]--><!--[if IE 8]><html class="a-no-js a-lt-ie10 a-lt-ie9 a-ie8" data-19ax5a9jf="dingo"><![endif]--><!--[if IE 9]><html class="a-no-js a-lt-ie10 a-ie9" data-19ax5a9jf="dingo"><![endif]--><!--[if !IE]><!--><html class="a-no-js" data-19ax5a9jf="dingo"><!--<![endif]--><head><script>var aPageStart = (new Date()).getTime();</script><meta charset="utf-8">
<script type='text/javascript'>var ue_t0=ue_t0||+new Date();</script>
<script type='text/javascript'>
var ue_csm = window,
    ue_hob = +new Date();

(function(a){var d=a.ue=a.ue||{},f=Date.now||function(){return+new Date};d.d=function(b){return f()-(b?0:a.ue_t0)};d.stub=function(b,c){if(!b[c]){var e=[];b[c]=function(){e.push([e.slice.call(arguments),d.d(),a.ue_id])};b[c].replay=function(b){for(var a;a=e.shift();)b(a[0],a[1],a[2])};b[c].isStub=1}}})(ue_csm);


    var ue_err_chan = 'jserr-rw';
(function(c,d){function e(f,b){if(!(a.ec>a.mxe)&&f){a.ec++;a.ter.push(f);b=b||{};var c=f.logLevel||b.logLevel;c&&c!=h||a.ecf++;b.pageURL=""+(d.location?d.location.href:"");b.logLevel=c;b.attribution=f.attribution||b.attribution;a.erl.push({ex:f,info:b})}}function g(a,b,d,e,g){c.ueLogError({m:a,f:b,l:d,c:""+e,err:g,fromOnError:1,args:arguments});return!1}var h="FATAL",a={ec:0,ecf:0,pec:0,ts:0,erl:[],ter:[],mxe:50,startTimer:function(){a.ts++;setInterval(function(){c.ue&&a.pec<a.ec&&c.uex("at");a.pec=
a.ec},1E4)}};g.skipTrace=1;e.skipTrace=1;e.isStub=1;c.ueLogError=e;c.ue_err=a;d.onerror=g})(ue_csm,window);


var ue_id = '0X849WPJZKXMCE756NPF',
    ue_url = '/mn/search/uedata/277-2541869-5922526',
    ue_navtiming = 1,
    ue_mid = 'A21TJRUUN4KGV',
    ue_sid = '277-2541869-5922526',
    ue_sn = 'www.amazon.in',
    ue_furl = 'fls-eu.amazon.com',
    ue_fcsn = 1,
    ue_fpf = '//fls-eu.amazon.com/1/batch/1/OP/A21TJRUUN4KGV:277-2541869-5922526:0X849WPJZKXMCE756NPF$uedata=s:',
    ue_swi = 1;

function ue_viz(){(function(c,e,p){function k(a){if(c.ue.viz.length<q&&!l){var b=a.type;a=a.originalEvent;/^focus./.test(b)&&a&&(a.toElement||a.fromElement||a.relatedTarget)||(b=e[m]||("blur"==b||"focusout"==b?"hidden":"visible"),c.ue.viz.push(b+":"+(+new Date-c.ue.t0)),"visible"==b&&(ue.isl&&uex("at"),l=1))}}for(var l=0,a,f,g,m,n=["webkit","o","ms","moz",""],d=0,q=20,h=0;h<n.length&&!d;h++)if(a=n[h],f=(a?a+"H":"h")+"idden",d="boolean"==typeof e[f])g=a+"visibilitychange",m=1!=p.ue_novizfix?(a?a+"V":
"v")+"isibilityState":a+"VisibilityState";k({});d&&e.addEventListener(g,k,0);c.ue&&d&&(c.ue.pageViz={event:g,propHid:f})})(ue_csm,document,window)};

(function(a,f){function v(a){return a&&a.replace&&a.replace(/^\s+|\s+$/g,"")}function p(a){return"undefined"===typeof a}function t(d,c,b,h){h=h||+new Date;var f,m;if(c||p(b)){if(d)for(m in f=c?g("t",c)||g("t",c,{}):a.ue.t,f[d]=h,b)b.hasOwnProperty(m)&&g(m,c,b[m]);return h}}function g(d,c,b){var f=a.ue,g=c&&c!=f.id?f.sc[c]:f;g||(g=f.sc[c]={});"id"==d&&b&&(f.cfa2=1,a.ue_ran&&a.ue_cel&&a.ue_cel.reset(b));return g[d]=b||g[d]}function z(d,c,b,f,g){b="on"+b;var m=c[b];"function"===typeof m?d&&(a.ue.h[d]=
m):m=function(){};c[b]=g?function(a){f(a);m(a)}:function(a){m(a);f(a)};c[b].isUeh=1}function A(d,c,b){function h(c,b){var e=[c],D=0,f={},m,h;b?(e.push("m=1"),f[b]=1):f=a.ue.sc;for(h in f)if(f.hasOwnProperty(h)){var k=g("wb",h),l=g("t",h)||{},q=g("t0",h)||a.ue.t0,n;if(b||2==k){k=k?D++:"";e.push("sc"+k+"="+h);for(n in l)3>=n.length&&!p(l[n])&&null!==l[n]&&e.push(n+k+"="+(l[n]-q));e.push("t"+k+"="+l[d]);if(g("ctb",h)||g("wb",h))m=1}}!w&&m&&e.push("ctb=1");return e.join("&")}function y(c,b,e,d){if(c){var g=
new Image,h=a.ue_err;if(!d||!a.ue.log||!f.amznJQ&&!f.P||f.amznJQ&&f.amznJQ.Ok)a.ue.iel.push(g),g.src=c;E?a.ue_fpf&&f.encodeURIComponent&&c&&(d=new Image,c=""+a.ue_fpf+f.encodeURIComponent(c)+":"+(+new Date-a.ue_t0),a.ue.iel.push(d),d.src=c):a.ue.log&&(g=f.chrome&&"ul"==b,a.ue.log(c,"uedata",a.ue_svi?{n:1,img:!d&&g?1:0}:{n:1}),a.ue.ielf.push(c));h&&!h.ts&&h.startTimer();a.ue.b&&(h=a.ue.b,a.ue.b="",y(h,b,e,1))}}function m(c){if(!ue.collected){var b=c.timing,e=c.navigation,d=ue.t;b&&(d.na_=b.navigationStart,
d.ul_=b.unloadEventStart,d._ul=b.unloadEventEnd,d.rd_=b.redirectStart,d._rd=b.redirectEnd,d.fe_=b.fetchStart,d.lk_=b.domainLookupStart,d._lk=b.domainLookupEnd,d.co_=b.connectStart,d._co=b.connectEnd,d.sc_=b.secureConnectionStart,d.rq_=b.requestStart,d.rs_=b.responseStart,d._rs=b.responseEnd,d.dl_=b.domLoading,d.di_=b.domInteractive,d.de_=b.domContentLoadedEventStart,d._de=b.domContentLoadedEventEnd,d._dc=b.domComplete,d.ld_=b.loadEventStart,d._ld=b.loadEventEnd,b=d.na_,c="function"!==typeof c.now||
p(b)?0:new Date(b+c.now())-new Date,d.ntd=c+a.ue.t0);e&&(d.ty=e.type+a.ue.t0,d.rc=e.redirectCount+a.ue.t0);ue.collected=1}}function s(b){var c=n&&n.navigation?n.navigation.type:x,d=c&&2!=c,e=a.ue.bfini;a.ue.cfa2||(e&&1<e&&(b+="&bfform=1",d||(a.ue.isBFT=e-1)),2==c&&(b+="&bfnt=1",a.ue.isBFT=a.ue.isBFT||1),a.ue.ssw&&a.ue.isBFT&&(p(a.ue.isNRBF)&&(c=a.ue.ssw(a.ue.oid),c.e||p(c.val)||(a.ue.isNRBF=1<c.val?0:1)),p(a.ue.isNRBF)||(b+="&nrbf="+a.ue.isNRBF)),a.ue.isBFT&&!a.ue.isNRBF&&(b+="&bft="+a.ue.isBFT));
return b}if(c||p(b)){for(var q in b)b.hasOwnProperty(q)&&g(q,c,b[q]);t("pc",c,b);q=g("id",c)||a.ue.id;var e=a.ue.url+"?"+d+"&v="+a.ue.v+"&id="+q,w=g("ctb",c)||g("wb",c),n=f.performance||f.webkitPerformance,k,l;w&&(e+="&ctb="+w);1<a.ueinit&&(e+="&ic="+a.ueinit);!a.ue._fi||"at"!=d||c&&c!=q||(e+=a.ue._fi());if(!("ld"!=d&&"ul"!=d||c&&c!=q)){if("ld"==d){f.onbeforeunload&&f.onbeforeunload.isUeh&&(f.onbeforeunload=null);if(f.chrome)for(l=0;l<ue.ulh.length;l++)B("beforeunload",ue.ulh[l]);(l=document.ue_backdetect)&&
l.ue_back&&l.ue_back.value++;a._uess&&(k=a._uess());a.ue.isl=1}a.ue_navtiming&&n&&n.timing&&(g("ctb",q,"1"),1==a.ue_navtiming&&t("tc",x,x,n.timing.navigationStart));n&&m(n);a.ue.t.hob=a.ue_hob;a.ue.t.hoe=a.ue_hoe;a.ue.ifr&&(e+="&ifr=1")}t(d,c,b);b="ld"==d&&c&&g("wb",c);var u;b?g("wb",c,2):"ld"==d&&(r.lid=v(q));for(u in a.ue.sc)if(1==g("wb",u))break;if(b){if(a.ue.s)return;e=h(e,null)}else l=h(e,null),l!=e&&(l=s(l),a.ue.b=l),k&&(e+=k),e=h(e,c||a.ue.id);e=s(e);if(a.ue.b||b)for(u in a.ue.sc)2==g("wb",
u)&&delete a.ue.sc[u];k=0;ue._rt&&(e+="&rt="+ue._rt());ue._bf&&(e+="&bf="+ue._bf());b||(a.ue.s=0,(k=a.ue_err)&&0<k.ec&&k.pec<k.ec&&(k.pec=k.ec,e+="&ec="+k.ec+"&ecf="+k.ecf),k=g("ctb",c),g("t",c,{}));e&&a.ue.tag&&0<a.ue.tag().length&&(e+="&csmtags="+a.ue.tag().join("|"),a.ue.tag=a.ue.tagC());e&&a.ue.viz&&0<a.ue.viz.length&&(e+="&viz="+a.ue.viz.join("|"),a.ue.viz=[]);e&&!p(a.ue_pty)&&(e+="&pty="+a.ue_pty+"&spty="+a.ue_spty+"&pti="+a.ue_pti);e&&a.ue.tabid&&(e+="&tid="+a.ue.tabid);e&&a.ue.aftb&&(e+="&aftb=1");
!a.ue._ui||c&&c!=q||(e+=a.ue._ui());a.ue.count&&1===a.ue_blc&&a.ue.count("baselineCounter1",1);a.ue.a=e;y(e,d,k,b)}}function s(a,c,b){b=b||f;b.addEventListener?b.addEventListener(a,c,!1):b.attachEvent&&b.attachEvent("on"+a,c)}function B(a,c,b){b=b||f;b.removeEventListener?b.removeEventListener(a,c,!1):b.detachEvent&&b.detachEvent("on"+a,c)}function C(){function d(){a.onUl()}function c(a){return function(){b[a]||(b[a]=1,A(a))}}var b=a.ue.r,g,p;a.onLd=c("ld");a.onLdEnd=c("ld");a.onUl=c("ul");g={stop:c("os")};
f.chrome?(s("beforeunload",d),ue.ulh.push(d)):g[F]=a.onUl;for(p in g)g.hasOwnProperty(p)&&z(0,f,p,g[p]);a.ue_viz&&ue_viz();s("load",a.onLd);t("ue")}a.ueinit=(a.ueinit||0)+1;var r={t0:f.aPageStart||a.ue_t0,id:a.ue_id,url:a.ue_url,rid:a.ue_id,a:"",b:"",h:{},r:{ld:0,oe:0,ul:0},s:1,t:{},sc:{},iel:[],ielf:[],fc_idx:{},viz:[],v:"0.383.21",d:a.ue&&a.ue.d,log:a.ue&&a.ue.log,onunload:a.ue&&a.ue.onunload,stub:a.ue&&a.ue.stub,lr:a.ue&&a.ue.lr,ulh:[],cfa2:0},E=a.ue_fpf?1:0,F="beforeunload",x;r.oid=v(r.id);r.lid=
v(r.id);a.ue=r;a.ue._t0=a.ue.t0;a.ue.tagC=function(){var a={};return function(c){c&&(a[c]=1);c=[];for(var b in a)a.hasOwnProperty(b)&&c.push(b);return c}};a.ue.tag=a.ue.tagC();a.ue.ifr=f.top!==f.self||f.frameElement?1:0;ue.attach=s;ue.detach=B;ue.reset=function(d,c){d&&(a.ue_cel&&a.ue_cel.reset(),a.ue.t0=+new Date,a.ue.rid=d,a.ue.id=d,a.ue.fc_idx={},a.ue.viz=[])};a.uei=C;a.ueh=z;a.ues=g;a.uet=t;a.uex=A;C()})(ue_csm,window);


ue.stub(ue,"log");ue.stub(ue,"onunload");

(function(g){var a=g.ue;a.cv={};a.cv.scopes={};a.count=function(d,e,b){var c={},f=a.cv;c.counter=d;c.value=e;c.t=a.d();b&&b.scope&&(f=a.cv.scopes[b.scope]=a.cv.scopes[b.scope]||{},c.scope=b.scope);if(void 0===e)return f[d];f[d]=e;a.log&&a.log(c,"csmcount",{c:1})};3===g.ue_blc&&a.count("baselineCounter2",1)})(ue_csm);


<!-- 7pmg0bk1lrmvlqc21ncqyyo3kk4yguvcv7cnz7phh2bh -->
</script>
<link rel="stylesheet" type="text/css" href="http://g-ecx.images-amazon.com/images/G/01/AUIClients/AmazonUI-8d3aa389bb3e27f422c5e89ce18f9f5b10736c15.rendering_engine-not-trident.weblab-AUI_FASTCLICK_47172-T1.min._V2_.css">
<link rel="stylesheet" type="text/css" href="http://g-ecx.images-amazon.com/images/G/01/AUIClients/RetailSearchAssets-57c866484f40334415221ca7189e731bc48468e5.in.renderskin-pc.search-results-aui.min._V2_.css">
<style type="text/css">
ul.s-result-list{margin:0 0 0 4px;padding:0;word-spacing:-4px;letter-spacing:-4px}ul.s-result-list li.s-result-item{display:inline-block;vertical-align:top;overflow:hidden;word-spacing:normal;letter-spacing:normal;padding:0;margin:0;zoom:1}ul.s-result-list li.s-result-item .s-item-container{padding:7px}ul.s-item-container-height-auto .s-item-container{height:auto!important}ul.s-result-list.s-list-mode li.s-result-item{width:100%!important}.a-ws ul.s-result-list.s-col-ws-1 li.s-result-item,ul.s-result-list.s-col-1 li.s-result-item{width:100%}.a-ws ul.s-result-list.s-col-ws-2 li.s-result-item,ul.s-result-list.s-col-2 li.s-result-item{width:50%}.a-ws ul.s-result-list.s-col-ws-2 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-2 li.s-result-item.s-col-span-2{width:100%}.a-ws ul.s-result-list.s-col-ws-3 li.s-result-item,ul.s-result-list.s-col-3 li.s-result-item{width:33.33333%}.a-ws ul.s-result-list.s-col-ws-3 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-3 li.s-result-item.s-col-span-2{width:66.66667%}.a-ws ul.s-result-list.s-col-ws-4 li.s-result-item,ul.s-result-list.s-col-4 li.s-result-item{width:25%}.a-ws ul.s-result-list.s-col-ws-4 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-4 li.s-result-item.s-col-span-2{width:50%}.a-ws ul.s-result-list.s-col-ws-5 li.s-result-item,ul.s-result-list.s-col-5 li.s-result-item{width:20%}.a-ws ul.s-result-list.s-col-ws-5 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-5 li.s-result-item.s-col-span-2{width:40%}.a-ws ul.s-result-list.s-col-ws-6 li.s-result-item,ul.s-result-list.s-col-6 li.s-result-item{width:16.66667%}.a-ws ul.s-result-list.s-col-ws-6 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-6 li.s-result-item.s-col-span-2{width:33.33333%}.a-ws ul.s-result-list.s-col-ws-7 li.s-result-item,ul.s-result-list.s-col-7 li.s-result-item{width:14.28571%}.a-ws ul.s-result-list.s-col-ws-7 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-7 li.s-result-item.s-col-span-2{width:28.57143%}.a-ws ul.s-result-list.s-col-ws-8 li.s-result-item,ul.s-result-list.s-col-8 li.s-result-item{width:12.5%}.a-ws ul.s-result-list.s-col-ws-8 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-8 li.s-result-item.s-col-span-2{width:25%}.a-ws ul.s-result-list.s-col-ws-9 li.s-result-item,ul.s-result-list.s-col-9 li.s-result-item{width:11.11111%}.a-ws ul.s-result-list.s-col-ws-9 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-9 li.s-result-item.s-col-span-2{width:22.22222%}.a-ws ul.s-result-list.s-col-ws-10 li.s-result-item,ul.s-result-list.s-col-10 li.s-result-item{width:10%}.a-ws ul.s-result-list.s-col-ws-10 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-10 li.s-result-item.s-col-span-2{width:20%}.a-ws ul.s-result-list.s-col-ws-11 li.s-result-item,ul.s-result-list.s-col-11 li.s-result-item{width:9.09091%}.a-ws ul.s-result-list.s-col-ws-11 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-11 li.s-result-item.s-col-span-2{width:18.18182%}.a-ws ul.s-result-list.s-col-ws-12 li.s-result-item,ul.s-result-list.s-col-12 li.s-result-item{width:8.33333%}.a-ws ul.s-result-list.s-col-ws-12 li.s-result-item.s-col-span-2,ul.s-result-list.s-col-12 li.s-result-item.s-col-span-2{width:16.66667%}.s-result-list-hgrid.s-col-1 li:nth-child(1n+2) .s-item-container,.s-result-list-hgrid.s-col-10 li:nth-child(1n+11) .s-item-container,.s-result-list-hgrid.s-col-11 li:nth-child(1n+12) .s-item-container,.s-result-list-hgrid.s-col-12 li:nth-child(1n+13) .s-item-container,.s-result-list-hgrid.s-col-2 li:nth-child(1n+3) .s-item-container,.s-result-list-hgrid.s-col-3 li:nth-child(1n+4) .s-item-container,.s-result-list-hgrid.s-col-4 li:nth-child(1n+5) .s-item-container,.s-result-list-hgrid.s-col-5 li:nth-child(1n+6) .s-item-container,.s-result-list-hgrid.s-col-6 li:nth-child(1n+7) .s-item-container,.s-result-list-hgrid.s-col-7 li:nth-child(1n+8) .s-item-container,.s-result-list-hgrid.s-col-8 li:nth-child(1n+9) .s-item-container,.s-result-list-hgrid.s-col-9 li:nth-child(1n+10) .s-item-container{border-top:1px solid #DDD}.a-ws ul.s-result-list-hgrid.s-col-ws-1 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-10 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-11 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-12 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-2 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-3 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-4 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-5 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-6 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-7 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-8 .s-result-item .s-item-container,.a-ws ul.s-result-list-hgrid.s-col-ws-9 .s-result-item .s-item-container{border-top-width:0}.a-ws .s-result-list-hgrid.s-col-ws-1 li:nth-child(1n+2) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-10 li:nth-child(1n+11) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-11 li:nth-child(1n+12) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-12 li:nth-child(1n+13) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-2 li:nth-child(1n+3) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-3 li:nth-child(1n+4) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-4 li:nth-child(1n+5) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-5 li:nth-child(1n+6) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-6 li:nth-child(1n+7) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-7 li:nth-child(1n+8) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-8 li:nth-child(1n+9) .s-item-container,.a-ws .s-result-list-hgrid.s-col-ws-9 li:nth-child(1n+10) .s-item-container{border-top:1px solid #DDD}.s-result-list-vgrid .s-item-container{border-left:1px solid #DDD}.s-col-1 .s-result-list-vgrid:nth-child(1n+1) .s-item-container,.s-col-10 .s-result-list-vgrid:nth-child(10n+1) .s-item-container,.s-col-11 .s-result-list-vgrid:nth-child(11n+1) .s-item-container,.s-col-12 .s-result-list-vgrid:nth-child(12n+1) .s-item-container,.s-col-2 .s-result-list-vgrid:nth-child(2n+1) .s-item-container,.s-col-3 .s-result-list-vgrid:nth-child(3n+1) .s-item-container,.s-col-4 .s-result-list-vgrid:nth-child(4n+1) .s-item-container,.s-col-5 .s-result-list-vgrid:nth-child(5n+1) .s-item-container,.s-col-6 .s-result-list-vgrid:nth-child(6n+1) .s-item-container,.s-col-7 .s-result-list-vgrid:nth-child(7n+1) .s-item-container,.s-col-8 .s-result-list-vgrid:nth-child(8n+1) .s-item-container,.s-col-9 .s-result-list-vgrid:nth-child(9n+1) .s-item-container{border-left-width:0}.a-ws ul.s-col-ws-1 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-10 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-11 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-12 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-2 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-3 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-4 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-5 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-6 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-7 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-8 li.s-result-list-vgrid div.s-item-container,.a-ws ul.s-col-ws-9 li.s-result-list-vgrid div.s-item-container{border-left:1px solid #DDD}.a-ws .s-col-ws-1 .s-result-list-vgrid:nth-child(1n+1) .s-item-container,.a-ws .s-col-ws-10 .s-result-list-vgrid:nth-child(10n+1) .s-item-container,.a-ws .s-col-ws-11 .s-result-list-vgrid:nth-child(11n+1) .s-item-container,.a-ws .s-col-ws-12 .s-result-list-vgrid:nth-child(12n+1) .s-item-container,.a-ws .s-col-ws-2 .s-result-list-vgrid:nth-child(2n+1) .s-item-container,.a-ws .s-col-ws-3 .s-result-list-vgrid:nth-child(3n+1) .s-item-container,.a-ws .s-col-ws-4 .s-result-list-vgrid:nth-child(4n+1) .s-item-container,.a-ws .s-col-ws-5 .s-result-list-vgrid:nth-child(5n+1) .s-item-container,.a-ws .s-col-ws-6 .s-result-list-vgrid:nth-child(6n+1) .s-item-container,.a-ws .s-col-ws-7 .s-result-list-vgrid:nth-child(7n+1) .s-item-container,.a-ws .s-col-ws-8 .s-result-list-vgrid:nth-child(8n+1) .s-item-container,.a-ws .s-col-ws-9 .s-result-list-vgrid:nth-child(9n+1) .s-item-container{border-left-width:0}li.s-result-item.s-item-placeholder.s-no-left .s-item-container{border-left:0!important}
</style>
<script>
(function(n,b,j,l){function i(a,b){A&&A.count&&A.count("aui:"+a,b||(A.count("aui:"+a)||0)+1)}function h(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function g(a,b,c,d){b=b&&c?b+a+c:b||c;return d?g(a,b,d):b}function k(a,b){try{Object.defineProperty(n,a,{value:b})}catch(c){n[a]=b}}function e(){return setTimeout(B,0)}function d(a,b){var c=a.length,d=c,f=function(){d--||(z.push(b),v||(e(),v=!0))};for(f();c--;)F[a[c]]?f():(m[a[c]]=m[a[c]]||[]).push(f)}function c(a,
c,d,e){var f=b.createElement(a?"script":"link");h(f,"error",e);a?(f.type="text/javascript",f.async=!0,d&&(c.indexOf("images/I")!==-1||/AUIClients/.test(c))&&f.setAttribute("crossorigin","anonymous"),f.src=c):(f.rel="stylesheet",f.href=c);b.getElementsByTagName("head")[0].appendChild(f)}function a(a,b){return function(d){function e(){c(b,d,f,function(){f?(f=!1,i("resource_retry"),e()):(i("resource_error"),a.log("Asset failed to load: "+d))})}if(E[d])return!1;E[d]=!0;i("resource_count");var f=!0;return!e()}}
function f(a,b,c,e,f){return function(g,h){var i=f||this;typeof g==="function"&&(h=g,g="anon"+L++);var j=i.guardError(g,function(){for(var c=[],d=0;d<a.length;d++)c[d]=K.hasOwnProperty(a[d])?K[a[d]]:l;d=null;e?d=h:typeof h==="function"&&(d=h.apply(n,c));if(b){K[g]=d;c=g;for(F[c]=!0;(m[c]||[]).length;)m[c].shift()();delete m[c]}});K.hasOwnProperty(g)&&i.error("Component already registered",g);K[g]=l;c?j():d(a,j)}}function o(a){return function(){return{execute:f(arguments,!1,a,!1,this),register:f(arguments,
!0,a,!1,this)}}}function p(a,b){return function(c,d){var e=this;return function(){d||(d=c,c=l);try{d.apply(this,arguments)}catch(f){var h=n.console;if(h&&h.error&&e.log(f,b,c))h.error(g(String.fromCharCode(10),g(": ",a,c,f.message),f.stack||f));else throw f instanceof Error?f:Error(g(": ",a,c,f));}}}}function r(b){this.log=function(a,c,d){var e=n.ueLogError;return e?(e({message:a,logLevel:c||"ERROR",attribution:g(":",b,d)}),!0):!1};this.error=function(a,c,d,e){throw Error(g(" @ ",g(":",e,a),g(":",
b,c,d)));};this.guardError=p(b);this.guardFatal=p(b,"FATAL");this.load={js:a(this,!0),css:a(this)}}function s(a,b){for(var c=a.className.split(" "),d=c.length;d--;)if(c[d]===b)return;a.className+=" "+b}function q(a,b){for(var c=a.className.split(" "),d=[],e;(e=c.pop())!==l;)e&&e!==b&&d.push(e);a.className=d.join(" ")}function w(a){try{return a()}catch(b){return!1}}function t(){if(ca){var a=n.innerWidth?{w:n.innerWidth,h:n.innerHeight}:{w:I.clientWidth,h:I.clientHeight},b=!1;Math.abs(a.w-Ma.w)>5||
a.h-Ma.h>50?(Ma=a,Na=4,(b=ja.mobile||ja.tablet?a.w>a.h:a.w>=1250)?s(I,"a-ws"):q(I,"a-ws")):Na--&&(ia=setTimeout(t,16))}}function u(){clearTimeout(ia);Na=4;t()}function y(a){(ca=a===l?!ca:!!a)&&t()}function x(){return ca}var D=n.AmazonUIPageJS||n.P;if(D&&D.when&&D.register)throw Error("A copy of P has already been loaded on this page.");var A=n.ue;A&&A.tag&&(A.tag("aui"),A.tag("aui:aui_build_date:3.15.3-2015-03-26"));var C=j.now=j.now||function(){return+new j},z=[],v=!1,B;B=function(){for(var a=e(),
b=C();z.length;)if(z.shift()(),C()-b>50)return;clearTimeout(a);v=!1};(function(a){try{return a.test(navigator.userAgent)}catch(b){return!1}})(/OS 6_[0-9]+ like Mac OS X/i)&&h(n,"scroll",e);var F={},m={},E={},L=0,K={},N;r.prototype={declare:f([],!0,!0,!0),register:f([],!0),execute:f([]),AUI_BUILD_DATE:"3.15.3-2015-03-26",when:o(),now:o(!0),trigger:function(a,b){var c=n.aPageStart||NaN,d=C(),c={data:b,pageElapsedTime:d-c,triggerTime:d};this.declare(a,c);N&&N(a,c)},handleTriggers:function(a){N&&this.error("Trigger handler already registered");
N=a},attributeErrors:function(a){return new r(a)}};k("AmazonUIPageJS",new r);k("P",n.AmazonUIPageJS);if(b.addEventListener){var J;b.addEventListener("DOMContentLoaded",J=function(){n.AmazonUIPageJS.trigger("a-domready");b.removeEventListener("DOMContentLoaded",J,!1)},!1)}var I=b.documentElement,H;try{H=navigator.userAgent}catch(Q){H=""}var Oa=function(){var a="Khtml,O,ms,Moz,Webkit".split(","),c=b.createElement("div");return{testGradients:function(){c.style.cssText=("background-image:"+"-webkit- ".split(" ").join("gradient(linear,left top,right bottom,from(#9f9),to(white));background-image:")+
a.join("linear-gradient(left top,#9f9, white);background-image:")).slice(0,-17);return c.style.backgroundImage.indexOf("gradient")>-1},test:function(b){for(var d=b.charAt(0).toUpperCase()+b.substr(1),b=(a.join(d+" ")+d+" "+b).split(" "),d=b.length;d--;)if(c.style[b[d]]==="")return!0;return!1},testTransform3d:function(){var a=!1;if(n.matchMedia)a=n.matchMedia("(-webkit-transform-3d)").matches;return a}}}(),ja={audio:function(){return!!b.createElement("audio").canPlayType},video:function(){return!!b.createElement("video").canPlayType},
canvas:function(){return!!b.createElement("canvas").getContext},offline:function(){return navigator.hasOwnProperty&&navigator.hasOwnProperty("onLine")&&navigator.onLine},dragDrop:function(){return"draggable"in b.createElement("span")},geolocation:function(){return!!navigator.geolocation},history:function(){return!(!n.history||!n.history.pushState)},autofocus:function(){return"autofocus"in b.createElement("input")},inputPlaceholder:function(){return"placeholder"in b.createElement("input")},textareaPlaceholder:function(){return"placeholder"in
b.createElement("textarea")},localStorage:function(){return"localStorage"in n&&n.localStorage!==null},orientation:function(){return"orientation"in n},touch:function(){return"ontouchend"in b},gradients:function(){return Oa.testGradients()},hires:function(){var a=n.devicePixelRatio&&n.devicePixelRatio>=1.5||n.matchMedia&&n.matchMedia("(min-resolution:144dpi)").matches,b=n.aPageStart;b&&(b=C()-b,i((a?"hi":"lo")+"ResInterval",b));return a},transform3d:function(){return Oa.testTransform3d()},touchScrolling:function(){return RegExp("Windowshop|android.([3-9]|[L-Z])|OS ([5-9]|[1-9][0-9]+)(_[0-9]{1,2})+ like Mac OS X|Chrome|Silk|Firefox|Trident"+
String.fromCharCode(92)+"/.+?; Touch","i").test(H)},ios:function(){return!!H.match(/OS [1-9][0-9]*(_[0-9]*)+ like Mac OS X/i)},android:function(){return!!H.match(/android.([1-9]|[L-Z])/i)&&!/trident/i.test(H)},mobile:function(){return/(^| )a-mobile( |$)/.test(I.className)},tablet:function(){return/(^| )a-tablet( |$)/.test(I.className)}},ha;for(ha in ja)ja.hasOwnProperty(ha)&&(ja[ha]=w(ja[ha]));for(var S="textShadow textStroke boxShadow borderRadius borderImage opacity transform transition".split(" "),
ma=0;ma<S.length;ma++)ja[S[ma]]=w(function(){return Oa.test(S[ma])});var ca=!0,ia=0,Ma={w:0,h:0},Na=4;t();typeof n.addEventListener==="function"?n.addEventListener("resize",u,!1):n.attachEvent("onresize",u);q(I,"a-no-js");s(I,"a-js");D=[];for(ha in ja)ja.hasOwnProperty(ha)&&ja[ha]&&D.push("a-"+ha.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()}));s(I,D.join(" "));I.setAttribute("data-aui-build-date",n.AmazonUIPageJS.AUI_BUILD_DATE);n.AmazonUIPageJS.register("p-detect",function(){return{capabilities:ja,
toggleResponsiveGrid:y,responsiveGridEnabled:x}})})(window,document,Date);
(function(){(function(){window.amzn=window.amzn||{};amzn.sx=amzn.sx||{};amzn.sx.utils=amzn.sx.utils||{};var b=amzn.sx.utils;if(!b.jsDepMgr)b.indexOf=b.indexOf||function(b,a){if(b.indexOf)return b.indexOf(a);for(var e=0;e<b.length;e++)if(b[e]===a)return e;return-1},b.jsDepMgr=new function(){var h={jQuery:function(){return window.jQuery}};this.when=function(a,e,g){function i(a,b,e,c,f){var d,g=b[0],j=b.length===1?function(){for(d=0;d<f.length;d++)f[d]=h[f[d]],f[d]&&f[d].call&&(f[d]=f[d]());try{c.apply(c,
f)}catch(a){throw a.message="["+e+"] "+a.message,window.ueLogError&&ueLogError(a),a;}}:function(){var d=b.slice(1);return function(){i(a,d,e,c,f)}}();amznJQ[a](g,j)}var c;typeof a==="string"&&(a=a.split(" "));c=b.indexOf(a,"jquery");c<0&&(c=b.indexOf(a,"$"));c>=0&&(a[c]="jQuery");window.amznJQ?(c=b.indexOf(a,"ready"),c!==-1&&(a=a.slice(0,c).concat(a.slice(c+1,a.length))),i(c!==-1?"onReady":"available",a,e,g,a)):P.when.apply(P,a).execute(function(){try{g.apply(this,arguments)}catch(a){throw a.message=
"["+e+"] "+a.message,window.ueLogError&&ueLogError(a),a;}})};this.register=function(a,b){window.amznJQ?(h[a]=b,amznJQ.declareAvailable(a)):P.register(a,b)}}})()})();
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('cf').execute(function() {(window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('http://g-ecx.images-amazon.com/images/G/01/AUIClients/AmazonUI-8ac7b1200ca3015408ab86f6089bb3ed6cc72c36.rendering_engine-not-trident.weblab-AUI_FASTCLICK_47172-T1.min._V2_.js');});
(window.AmazonUIPageJS ? AmazonUIPageJS : P).when('cf').execute(function() {(window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('http://g-ecx.images-amazon.com/images/G/01/AUIClients/RetailSearchAssets-1ea179f15680c83401dc02aff9356e31a26424a9.in.renderskin-pc.search-results-aui.min._V2_.js');});
(function(q){q.execute(function(){q.execute("sxResultListLibrary",function(){function d(a){return typeof a==="number"&&a%1===0}function g(a,b){var c,d=[],f;if(a.className){c=a.className.split(" ");for(f=0;f<c.length;f++)c[f].indexOf(b)!==0&&d.push(c[f]);a.className=d.join(" ")}}function c(a,b){var c=null,f=-1;if(!a)return null;for(var g in a)if(a.hasOwnProperty(g)){var h=a[g],i=parseInt(g,10);if(!d(h)||h<1||h>12||isNaN(i)||i<0)return;b>=i&&i>=f&&(c=h,f=i)}return c}function a(a,b){var c=t+b,d=a.className&&
a.className.indexOf(c)>-1;g(a,s);if(!d)g(a,t),a.className=a.className+" "+c;return!d}function b(a){for(;a&&a.parentNode;)if(a=a.parentNode,a.className&&a.className.indexOf(n)>-1&&a.clientWidth)return a.clientWidth;return window.document.documentElement.clientWidth}function f(d,f){var g=document.getElementById(d),h=b(g),h=c(f,h);g&&h&&a(g,h)}var i="s-result-list",h="s-result-list-hgrid",j="s-result-list-vgrid",k=" s-no-left",m="s-item-container-height-auto",l="s-item-container",o="s-height-equalized",
p="s-item-placeholder",n="s-result-list-parent-container",t="s-col-",s="s-col-ws-",r=['<li class="s-result-item '+p,k,'"><div class="s-item-container"',"></div></li>"],u=[r[0],r[1]," "+j,r[2],' style="height: ',"",'px"',r[3]];q.register("s-result-list-core",function(){return{initList:f}});q.when("A").register("s-result-list-util",function(f){function n(a){return a.hasClass(i)}function q(){return fa.hasClass("a-ws")}function D(a,b,c){a-=b;return(c-a%c)%c-b}function H(a){var b={},a=a.attr("class").split(/\s+/);
V.each(a,function(a,c){if(c.indexOf(s)===0)b.wsCol=parseInt(c.slice(s.length),10);else if(c.indexOf(t)===0)b.col=parseInt(c.slice(t.length),10)});return b}function F(a){return a.data(p)}function C(a){return a.data("columns")}function L(a,c){var d=a.data("containerWidth");if(c||!d)d=b(a.get(0)),a.data("containerWidth",d);return d}function ca(a,b,c){var d=F(a),f,g=[];if(!(d&&d.usePlaceholders===!1)){f=a.children("li");if(!d)d={hGrid:a.hasClass(h),vGrid:V(f[0]).hasClass(j),height:V(f[0]).find(".s-item-container").height(),
placeholders:0},d.usePlaceholders=d.hGrid||d.vGrid,d=V.extend(d,H(a)),a.data(p,d);if(d.usePlaceholders){b=b||c&&d.wsCol||d.col;b=D(f.length,d.placeholders,b);if(b>0){f=r;if(d.vGrid)f=u,f[5]=d.height;for(c=0;c<b;c++)f[1]=c===0&&d.placeholders===0?"":k,V.merge(g,f);V(g.join("")).appendTo(a)}else b<0&&f.slice(f.length+b,f.length).remove();d.placeholders+=b;a.data(p,d)}}}function T(a,b){var d=V(a),f;if(n(d)){f=d.data(p);d.children("."+p).remove();if(f)f.placeholders=0;b(d);f=c(C(d),L(d));ca(d,f,q());
ba(d)&&(x(d),f||(f=H(d)[q?"wsCol":"col"]),$(d,f))}}function ba(a){return a.hasClass(o)}function x(a){var b=a.find("li > ."+l).get();a.data("bogons",b);return b}function $(a,b){if(!(b<=1)){var c=a.data("bogons"),d=V([1]),f,g,h,i=0;c||(c=x(a));if(c.length!==0){a.addClass(m);for(f=0;f<c.length;f+=b){h=f+Math.min(b,c.length-f);i=0;for(g=f;g<h;g++)d[0]=c[g],i=Math.max(i,d.outerHeight());for(g=f;g<h;g++)d[0]=c[g],d.height(i)}a.removeClass(m)}}}var V=f.$,fa=V("html");return{isInt:d,removeClassPrefix:g,isResultList:n,
setListMode:function(a,b){var c=V("#"+a);n(c)&&c.toggleClass("s-list-mode",b?!0:!1)},getColumns:c,setColumns:a,getColumnData:C,getConfiguredColumns:function(a){a=H(V(a));return a.wsCol&&q()?a.wsCol:a.col},isWs:q,getPlaceholderData:F,getPlaceholderDelta:D,updatePlaceholders:ca,appendItems:function(a,b){T(a,function(a){a.append(b)})},modifyList:T,size:function(a){return V(a).children().not("."+p).length},getEventName:function(a){return"s:result-list:"+V(a).attr("id")+":columns-changed"},isHeightEqualized:ba,
equalizeContainerHeights:$,getColumnCssSettings:H,getContainerWidth:L}})});q.when("A","s-result-list-util").register("s-result-list",function(d,g){function c(){var c,h,j=a([1]),k,m,l=g.isWs();for(c=0;c<b.length;c++)if(h=b[c],j[0]=h,m=!1,g.isResultList(j)){(k=g.getColumns(g.getColumnData(j),g.getContainerWidth(j,!0)))&&(m=g.setColumns(h,k));if(m||l!==f)d.trigger(g.getEventName(j),j,g.getConfiguredColumns(h)),g.updatePlaceholders(j,k,l);g.isHeightEqualized(j)&&(k||(k=g.getColumnCssSettings(j)[l?"wsCol":
"col"]),g.equalizeContainerHeights(j,k))}f=l}var a=d.$,b=document.getElementsByTagName("ul"),f=null;c();d.on.resize(c);d.on.orientationchange(c);d.interval(function(){c()},2E3);d.declarative("set-result-list-mode","click",function(b){g.setListMode(a(b.data.id),b.data.listMode)});return{refresh:c,size:g.size,columns:g.getConfiguredColumns,appendItems:g.appendItems,modifyList:g.modifyList,setListMode:g.setListMode,getColumnsChangedEvent:g.getEventName}})})})(function(){var q=window.AmazonUIPageJS||
P,d=q.attributeErrors;return d?d("RetailSearchResultListAssets"):q}());
</script>
<script type="text/javascript">
var search_t0 = window.ue_t0 || + new Date();
</script>
<style type="text/css">
.s-icon, .currencyINR, .srSprite {
    background-image: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/gui/searchSprite._CB323617840_.png);
}

#leftNav div.buttonsprite div {
    background-image: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/gui/searchSprite._CB323617840_.png);
}

#leftNav li.subgroup a span.expand {
    background: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/gui/searchSprite._CB323617840_.png) no-repeat scroll -143px -821px;
}

#leftNav li.subgroup a span.collapse {
    background: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/gui/searchSprite._CB323617840_.png) no-repeat scroll -132px -821px;
}

.s-icon-badging-sticker-ellipse {
    background-image: url();
}

.s-icon-badging-sticker-sash {
    background-image: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/sticker/sx-x-trapezoid._CB320906722_.png);
}

.s-icon-ags {
  background-image: url();
}

.sortSprite {
  background-image: url();
}

.s-icon-holiday-toy-list {
  background-image: url();
}

.s-badges-background-tl {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/sticker/sx-badges-pc._CB329918278_.png);
}

.s-badges-background-bl {
  background-image: url();
}

.s-softlines-federation-sprite {
  background-image: url();
}
</style>
<title>Amazon.in: smartphones</title>

<meta name="description" content="Amazon.in: smartphones" />
<meta name="keywords" content="smartphones, Amazon.in" />
<link rel="canonical" href="http://www.amazon.in/smartphones/s?ie=UTF8&amp;page=1&amp;rh=i%3Aaps%2Ck%3Asmartphones" />
<link rel="dns-prefetch" href="ecx.images-amazon.com" />
    <link rel="dns-prefetch" href="g-ecx.images-amazon.com" />
    <link rel="dns-prefetch" href="z-ecx.images-amazon.com" />





<!-- nav-config-asset-injection IN::desktop::standard::49573:C&42994:T1&42980:C::auiDebug=0::isSecure=0::jsOnEvent= navc-0TaMIZdXR5JU8dpmI89FCC90yKt7MOtvZGstex6C7oTu9oikDkNCDA== rid-6D4A470BD0B743679486 seq-214 (Sat May 16 02:44:58 2015) **CACHED-BY-NCCC** -->
<link rel="stylesheet" href="http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavAuiAssets-4c6327e530fbf6448291efaf91a613db0dd48b96.min._V2_.css" />
<link rel="stylesheet" href="http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavMetaAsset-fa7f4967b0f2d023988c5d05762ecf8e9c981e87._V2_.css" />
<script type='text/javascript'>

(function(d,c){function f(a){b.push(a)}function e(a){if(a){var c=d.head||d.getElementsByTagName("head")[0]||d.documentElement,b=d.createElement("script");b.async="async";b.src=a;c.insertBefore(b,c.firstChild)}}function g(){ue.uels=e;for(var a=0;a<b.length;a++)e(b[a]);ue.deffered=1}var b=[];c.ue&&(ue.uels=f,c.ue.attach&&c.ue.attach("load",g))})(document,window);

(function(a){var b=a.alert;window.alert=function(){a.ueLogError&&a.ueLogError({message:"[CSM] Alert invocation detected with argument: "+arguments[0],logLevel:"WARN"});Function.prototype.apply.apply(b,[a,arguments||[]])}})(window);

(function(d,r,k){function l(a){if(!b)if(b=e[a.type],"undefined"===typeof a.clientX?(f=a.pageX,g=a.pageY):(f=a.clientX,g=a.clientY),2!=b||h&&(h!=f||m!=g)){for(var d in e)e.hasOwnProperty(d)&&c.detach(d,l,k);c.isl&&r.setTimeout(function(){n("at",c.id)},0)}else h=f,m=g,b=0}function s(){var a="";!p&&b&&(p=1,a+="&ui="+b);return a}var c=d.ue,n=d.uex,p=0,b=0,h,m,f,g,e={click:1,mousemove:2,scroll:3,keydown:4};if(c&&n){for(var q in e)e.hasOwnProperty(q)&&c.attach(q,l,k);c._ui=s}})(ue_csm,window,document);



if (window.ue && window.ue.uels) {
    ue.uels("http://g-ecx.images-amazon.com/images/G/01/browser-scripts/forester-client/forester-client-min-758617388.js");

        ue.uels("http://g-ecx.images-amazon.com/images/G/01/browser-scripts/jserrors/jserrors-min-3018617914.js");

}

(function(k,c){function l(a,b){return a.filter(function(a){return a.initiatorType==b})}function f(a,c){if(b.t[a]){var g=b.t[a]-b._t0,e=c.filter(function(a){return 0!==a.responseEnd&&m(a)<g}),f=l(e,"script"),h=l(e,"link"),k=l(e,"img"),n=e.map(function(a){return a.name.split("/")[2]}).filter(function(a,b,c){return a&&c.lastIndexOf(a)==b}),q=e.filter(function(a){return a.duration<p}),s=g-Math.max.apply(null,e.map(m))<r|0;"af"==a&&(b._afjs=f.length);return a+":"+[e[d],f[d],h[d],k[d],n[d],q[d],s].join("-")}}
function m(a){return a.responseEnd-(b._t0-c.timing.navigationStart)}function n(){var a=c[h]("resource"),d=f("cf",a),g=f("af",a),a=f("ld",a);delete b._rt;b._ld=b.t.ld-b._t0;b._art&&b._art();return[d,g,a].join("_")}var p=20,r=50,d="length",b=k.ue,h="getEntriesByType";b._rre=m;b._rt=c&&c.timing&&c[h]&&n})(ue_csm,window.performance);



    var ue_tbno = 1,
        ue_tble = 0;

(function(d,k){function e(d){var c;c="";var b=a.isBFT?"b":"s",e=""+a.oid,f=""+a.lid,g=e;e!=f&&20==f.length&&(b+="a",g+="-"+f);q&&a.tabid&&(c=a.tabid+"+");c+=b+"-"+g;(l||c!=h)&&100>c.length&&(h=c,document.cookie="csm-hit="+c+("|"+ +new Date)+r+"; path=/");m&&a.log&&a.log(""+(d?d.type:"interaction")+" "+c,"csm")}function n(){h=0;m&&a.log&&a.log("blur","csm")}function p(b){!0===k[a.pageViz.propHid]?n():!1===k[a.pageViz.propHid]&&e({type:"visible"})}var r="; expires="+(new Date(+new Date+6048E5)).toGMTString(),
h,q=d.ue_sstb,l=d.ue_tbno,m=d.ue_tble,b=d.ue_tbpv,a=d.ue||{},f=b&&a.pageViz&&a.pageViz.event&&a.pageViz.propHid;a.attach&&(a.attach("click",e),a.attach("keyup",e),l||(f&&4!=b&&5!=b||(a.attach("focus",e),a.attach("blur",n)),f&&a.attach(a.pageViz.event,p),!f||3!=b&&5!=b||p({})));a.aftb=1})(ue_csm,document);



if(window.ue&&ue.t) { uet('bb'); }

var ue_hoe = +new Date();
</script>
</head><body class="a-aui_bolt_46632-c a-aui_ux_45508-c a-aui_ux_45669-c"><div id="a-page"><script type="a-state" data-a-state="{&quot;key&quot;:&quot;a-wlab-states&quot;}">{"AUI_BOLT_46632":"C","AUI_UX_45508":"C","AUI_UX_45669":"C"}</script>

<script type='text/javascript'>

(function(){function g(n){for(var b=a.location.search.substring(1).split("&"),d=0;d<b.length;d++){var c=b[d].split("=");if(c[0]===n)return c[1]}}window.amzn=window.amzn||{};amzn.copilot=amzn.copilot||{};var a=window,b=document,h=b.head||b.getElementsByTagName("head")[0],k=0,l=0;amzn.copilot.checkCoPilotSession=function(){b.cookie.match("cpidv")&&("undefined"!==typeof jQuery&&f(jQuery),a.P&&a.P.when&&a.P.when("jQuery").execute(function(a){f(a)}),a.amznJQ&&a.amznJQ.available&&a.amznJQ.available("jQuery",
function(){f(jQuery)}),a.jQuery||a.P||a.amznJQ||p())};var p=function(){k?a.ue&&"function"===typeof a.ue.count&&a.ue.count("cpJQUnavailable",1):(k=1,b.addEventListener?b.addEventListener("DOMContentLoaded",amzn.copilot.checkCoPilotSession,!1):b.attachEvent&&b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&amzn.copilot.checkCoPilotSession()}))},f=function(b){if(!l){l=1;amzn.copilot.jQuery=b;b=g("debugJS");var e="https:"===a.location.protocol?1:0,d="/gp/copilot/handlers/copilot_strings_resources.html";
window.texas&&texas.locations&&(d=texas.locations.makeUrl(d));amzn.copilot.jQuery.ajax&&amzn.copilot.jQuery.ajax({url:d,dataType:"json",data:{isDebug:b,isSecure:e},success:function(a){amzn.copilot.vip=a.serviceEndPoint;q(a)},error:function(){a.ue.count("cpLoadResourceError",1)}})}},q=function(a){var e=amzn.copilot.jQuery,d=function(){amzn.copilot.setup(e.extend({isContinuedSession:!0},a))};e.each(a.CSSUrls[0],function(a,d){var c=b.createElement("link");c.type="text/css";c.rel="stylesheet";c.href=
d;h.appendChild(c)});var c=g("forceSynchronousJS"),f=a.JSUrls[0];e.each(f,function(a,b){a===f.length-1?m(b,c,d):m(b,c)})},m=function(a,e,d){var c=b.createElement("script");c.type="text/javascript";c.src=a;c.async=e?!1:!0;d&&(c.onload=d);h.appendChild(c)}})();

amzn.copilot.checkCoPilotSession();

</script>
<style type="text/css"><!--
.nav-sprite-v1 .nav-sprite {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-v1._CB333157339_.png);
  background-position: 0 1000px;
  background-repeat: repeat-x;
}
.nav-spinner {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/javascripts/lib/popover/images/snake._CB138350263_.gif);
}
.nav-ajax-loading .nav-ajax-message {
  background: center center url(http://g-ecx.images-amazon.com/images/G/31/javascripts/lib/popover/images/snake._CB138350263_.gif) no-repeat;
}
.iss-sprite {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/nav2/images/gui/beacon-sprite.png);
}
.nav-xshop-small .nav-cobrand {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/gno/images/irctc/IRCTC_Logo-small._CB329403128_.png);
}
.nav-xshop-large .nav-cobrand {
  background-image: url(http://g-ecx.images-amazon.com/images/G/31/gno/images/irctc/IRCTC_Logo._CB329403128_.png);
}

--></style>

<!-- From remote config v3-->
<script type="text/javascript">
(function(b){document.createElement("header");var d=function(b){function c(c,e,b){c[b]=function(){a._replay.push(e.concat({m:b,a:[].slice.call(arguments)}))}}var a={};a._sourceName=b;a._replay=[];a.getNow=function(a,c){return c};a.when=function(){var a=[{m:"when",a:[].slice.call(arguments)}],b={};c(b,a,"run");c(b,a,"declare");c(b,a,"publish");c(b,a,"build");return b};c(a,[],"declare");c(a,[],"build");c(a,[],"publish");c(a,[],"importEvent");d._shims.push(a);return a};d._shims=[];b.$Nav||(b.$Nav=d("rcx-nav"));
b.$Nav.make||(b.$Nav.make=d)})(window);

window.amznJQ && amznJQ.available('navbarJS-global', function(){});
window._navbarSpriteUrl = 'http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-v1._CB333157339_.png';
$Nav.importEvent('navbarJS-global');
$Nav.importEvent('NavAuiAssets');
$Nav.declare('img.pixel', 'http://g-ecx.images-amazon.com/images/G/31/x-locale/common/transparent-pixel._CB386942716_.gif');
$Nav.declare('img.sprite', {
  'png8': 'http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-v1._CB333157339_.png',
  'png32': 'http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-32-v1._CB332848083_.png',
  'png32-2x': 'http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-32-2x-v1._CB333157332_.png'
});
</script>
<img src="http://g-ecx.images-amazon.com/images/G/31/gno/sprites/global-sprite-v1._CB333157339_.png" style="display:none" alt=""/>
<img src="http://g-ecx.images-amazon.com/images/G/31/x-locale/common/transparent-pixel._CB386942716_.gif" style="display:none" alt="" id="nav_trans_pixel"/>

<!-- nav-config-asset-injection no-aui-p -->
<!-- nav-config-asset-injection IN::desktop::standard::49573:C&42994:T1&42980:C::auiDebug=0::isSecure=0::jsOnEvent= navc-0TaMIZdXR5JU8dpmI89FCC90yKt7MOtvZGstex6C7oTu9oikDkNCDA== rid-6D4A470BD0B743679486 seq-214 (Sat May 16 02:44:58 2015) **CACHED-BY-NCCC** -->
<script>
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavAuiAssets-a34aa87bb465b562264bb7662feb97e6f357dca0.min._V2_.js');
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).load.js('http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavMetaAsset-bdbf725d2dcb9712aa9253bc09af97731b74148f._V2_.js');
</script>




















<!--Pilu -->





<script type='text/javascript'>
window.uet && uet('ns');

window._navbar = (function (o) {
  o.componentLoaded = o.loading = function(){};
  o.browsepromos = {};
  o.issPromos = [];
  return o;
}(window._navbar || {}));

window.$Nav && $Nav.declare('logEvent.enabled',
  false);


window.$Nav && $Nav.declare('config.lightningDeals',{});
window.$Nav && $Nav.declare('config.swmStyleData',{});
window.$Nav && $Nav.declare('config.ajaxProximity', [141,7,60,150]);

</script>

<!-- navp-UY3HNjt0yw8LNf9ecABPOKa5ZWHpmpdG5YpA19L+utV42pejlfUQ7w== rid-0X849WPJZKXMCE756NPF (Sat May 16 03:27:49 2015) -->



<![if gt IE 6]><noscript><![endif]>
<style type="text/css"><!--
    #navbar select#searchDropdownBox {
      visibility: visible;
      display: block;
    }
    #navbar #nav-search-in {
      width: 200px;
    }
    #navbar #nav-search-in-content {
      display: none;
    }
--></style>
<![if gt IE 6]></noscript><![endif]>
<style type="text/css"><!--#nav-bar-middle #nav-searchbar .nav-submit-button .nav-submit-input {
    margin: 0;
    padding: 0px 11px;
}
--></style>

<header class='nav-locale-in nav-lang-en'>

  <div id='navbar' role="navigation" class='nav-subnav-container nav-skin-default nav-sprite-v1'>






    <div id='nav-cross-shop' class='nav-xshop-large'>


<div id='nav-logo' >
  <a href="/ref=nav_logo" class='nav-logo-link'>
    <span class='nav-logo-base nav-sprite'>Amazon</span>
    <span class='nav-logo-ext nav-sprite'></span>
    <span class='nav-logo-locale nav-sprite'></span>
  </a>
  <a href="/ref=nav_logo" class='nav-logo-tagline nav-sprite'></a>
</div>



      <div id='nav-cross-shop-content'>



    <div id='nav-cross-shop-links'>
      <a href='/gp/yourstore/home/ref=nav_cs_ys' class='nav_a' id='nav-your-amazon'>Your Amazon.in</a><a href='/gp/goldbox/ref=nav_topnav_deals' class='nav_a'>Today's Deals</a><a href='/gift-card-store/b/ref=nav_topnav_giftcert?ie=UTF8&node=3704982031' class='nav_a'>Gift Cards</a><a href='/b/ref=nav_topnav_sell?ie=UTF8&node=2838698031' class='nav_a'>Sell</a><a href='/gp/help/customer/display.html/ref=nav_topnav_help?ie=UTF8&nodeId=200507590' class='nav_a'>Customer Service</a><a href="/app-nav?_encoding=UTF8&amp;ref=nav_topnav_app_icon" id="nav-transient-flyout-trigger" style="float: left;width: 24px;height: 24px; padding-left:6px; margin-top:-10px; padding-right:2px;background: url(&#39;http://g-ecx.images-amazon.com/images/G/31/img13/mshop/nav/mobile_app_download_icon-1._V327620770_.png&#39;) no-repeat;"></a>
    </div>

      </div>


        <div id='welcomeRowTable' style='height:50px'>
        <div id='nav-ad-background-style' style='background-position: -800px 0px; background-image: url(http://g-ecx.images-amazon.com/images/G/31/2015/Deals/April/HappyHour/Teaser1/PC/300x50_SWM-Slot._V306315487_.jpg);  height: 56px; margin-bottom: -6px; position: relative;background-repeat: no-repeat;'>
          <div id='navSwmSlot'>
            <div id="navSwmHoliday" style="background-image: url(http://g-ecx.images-amazon.com/images/G/31/2015/Deals/April/HappyHour/Teaser2/300x50_SWM-Slot._V306315698_.jpg); width: 300px; height: 50px; overflow: hidden;"><img alt='Appy Hour' src='http://g-ecx.images-amazon.com/images/G/31/x-locale/common/transparent-pixel._V386942716_.gif' border='0' width='300px' height='50px' usemap='#nav-swm-holiday-map' /></div><div style="display: none;"><map id="nav-swm-holiday-map" name="nav-swm-holiday-map"><area shape="rect" coords="1,2,300,50" href ="/gp/feature.html/ref=sweeps_swm?ie=UTF8&docId=1000809793&pf_rd_p=607685627&pf_rd_s=nav-sitewide-msg&pf_rd_t=4201&pf_rd_i=navbar-4201&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=0X849WPJZKXMCE756NPF" alt ="Appy Hour" /></map></div>
          </div>
        </div>
      </div>
    </div>

    <div id='nav-bar-outer'>

      <div id='nav-logo-borderfade'><div class='nav-fade-mask'></div><div class='nav-fade nav-sprite'></div></div>

      <div id='nav-bar-inner' class="nav-sprite">

        <div id='nav-bar-left'>
          <a id='nav-shop-all-button' href="/gp/site-directory/ref=nav_sad" class='nav_a nav-button-outer nav-menu-inactive' alt="Shop By Department">
            <span class='nav-button-title nav-button-line1'>Shop by</span>
            <span class='nav-button-title nav-button-line2'>Department<span class='nav-down-arrow'></span></span>
          </a>
        </div>

        <div id='nav-bar-right'>


          <a id='nav-your-account' href="https://www.amazon.in/ap/signin?_encoding=UTF8&amp;openid.assoc_handle=inflex&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&amp;openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Fie%3DUTF8%26ref_%3Dnav_yam_ya" class='nav_a nav-button-outer nav-menu-inactive' alt="Your Orders">
            <span id='nav-signin-title' class='nav-button-title nav-button-line1'  >
              Hello.
              <span id='nav-signin-text' class='nav-button-em'>Sign in</span>
            </span>
            <span class='nav-button-title nav-button-line2'>Your Orders<span class='nav-down-arrow'></span></span>
          </a>

        <span class='nav-divider'></span>
<a id='nav-cart' href='/gp/cart/view.html/ref=nav_cart' class='nav_a nav-button-outer nav-menu-inactive' alt='Shopping Cart'>
  <span class='nav-button-title nav-button-line1'> </span>
  <span class='nav-button-title nav-button-line2'>Cart<span class='nav-down-arrow'></span></span>
  <span class='nav-cart-button nav-sprite'></span>
  <span id='nav-cart-count' class='nav-cart-0'>0 </span>
</a>
<span class='nav-divider'></span>
<a id='nav-wishlist' href='/gp/registry/wishlist/ref=nav_wish_list' class='nav_a nav-button-outer nav-menu-inactive' alt='Wish List'>
  <span class='nav-button-title nav-button-line1'>Wish</span>
  <span class='nav-button-title nav-button-line2'>List<span class='nav-down-arrow'></span></span>
</a>

        </div>

        <div id='nav-bar-middle'>
                      <label id='nav-search-label' for='twotabsearchtextbox'>
              Search
            </label>
                    <form
            id='nav-searchbar'
            action="/s/ref=nb_sb_noss"
            method='get' name='site-search'
            role='search'
            accept-charset='utf-8',
            class='nav-searchbar-inner'
          >


            <div class='nav-submit-button nav-sprite'>
              <input
                type='submit'
                value="Go"
                class='nav-submit-input'
                title="Go"
              >
            </div>

            <span id='nav-search-in' class='nav-sprite'>
              <span id='nav-search-in-content' data-value="search-alias=aps">
                All
              </span>
              <span class='nav-down-arrow'></span>
              <select class="searchSelect" data-nav-digest="j6hJTM0VLm6q5VrT9gU97rVLmvg" data-nav-selected="0" id="searchDropdownBox" name="url" title="Search in">
<option selected="selected" value="search-alias=aps">All Departments</option>
<option value="search-alias=baby">Baby</option>
<option value="search-alias=beauty">Beauty</option>
<option value="search-alias=stripbooks">Books</option>
<option value="search-alias=automotive">Car & Motorbike</option>
<option value="search-alias=apparel">Clothing & Accessories</option>
<option value="search-alias=computers">Computers & Accessories</option>
<option value="search-alias=electronics">Electronics</option>
<option value="search-alias=gift-cards">Gift Cards</option>
<option value="search-alias=grocery">Gourmet & Specialty Foods</option>
<option value="search-alias=hpc">Health & Personal Care</option>
<option value="search-alias=kitchen">Home & Kitchen</option>
<option value="search-alias=jewelry">Jewellery</option>
<option value="search-alias=digital-text">Kindle Store</option>
<option value="search-alias=everyday-essentials">KiranaNow</option>
<option value="search-alias=luggage">Luggage & Bags</option>
<option value="search-alias=dvd">Movies & TV Shows</option>
<option value="search-alias=popular">Music</option>
<option value="search-alias=mi">Musical Instruments</option>
<option value="search-alias=office-products">Office Products</option>
<option value="search-alias=pets">Pet Supplies</option>
<option value="search-alias=shoes">Shoes & Handbags</option>
<option value="search-alias=software">Software</option>
<option value="search-alias=sporting">Sports, Fitness & Outdoors</option>
<option value="search-alias=toys">Toys & Games</option>
<option value="search-alias=videogames">Video Games</option>
<option value="search-alias=watches">Watches</option>
</select>
            </span>

            <div class='nav-searchfield-width'>
              <div id='nav-iss-attach'>
                <input type='text' id='twotabsearchtextbox' title="Search For" value="smartphones" name='field-keywords' autocomplete='off'>
              </div>
            </div>
          </form>
        </div>

</div><div id="nav-subnav-container"  style='display: none;'>
          <ul id='nav-subnav'  style='display: none;' data-category="gateway" data-digest="0">
<li class="nav-subnav-item nav-category-button"><a href="#" class="nav_a"></a></li><li class="nav-subnav-item"><a class="nav_a"></a></li><li class="nav-subnav-item"><a class="nav_a"></a></li>          </ul>
      </div>
    </div>


  </div>
</header>


<style>
#nav-transient-flyout {padding:0px;
 margin-left:4px !important;
}
#nav-transient-flyout h3 {
  font: 15px arial, sans-serif;
  color:#e47911;
  margin: 5px 0;
}
 #nav-transient-flyout input{font-size:12px;
 font-family: arial, sans-serif;
 width:150px;
height:30px;
 border color:#border-color:#a88734;
background-color:#f3d078;
border-color:#f3d078; border-style:solid;
border-radius:3px;
 background-image: -webkit-linear-gradient(top, #f7dfa5,#f0c14b);
 background-image: -moz-linear-gradient(top, #f7dfa5,#f0c14b);
 background-image: -ms-linear-gradient(top, #f7dfa5,#f0c14b);
 background-image: -o-linear-gradient(top, #f7dfa5,#f0c14b);
 background-image: linear-gradient(to bottom, #f7dfa5,#f0c14b);
 text-decoration:none !important;
}
 #nav-transient-flyout a{
 text-decoration:none;
}
#nav-transient-flyout a:hover{
 text-decoration:none !important;
}
</style>
<script type="text/javascript">
  window.$Nav && $Nav.declare('flyouts.transient', {"html":"<div id=\"nav-transient-flyout\"><h3><p style=\"text-align: center;\">SHOP ANYWHERE. ANYTIME.</p></h3><p style=\"text-align: center;\"><a href=\"/app-nav?ref=nav_topnav_app_flyout_button\"><input type=\"button\" value=\"Download the App\"/></a><p style=\"text-align: center;\"><a href=\"/app-nav?ref=nav_topnav_app_flyout_img\"><img src='http://g-ecx.images-amazon.com/images/G/31/img13/mshop/nav/mobile_app_download_flyout.png'></p></a></div>"});
</script>


<!-- nav promo cached -->


<map name="nav_imgmap_amazon-apps" id="nav_imgmap_amazon-apps">
<area shape="rect" coords="0,35,485,380" href="/gp/feature.html/ref=sweeps_flyout?ie=UTF8&docId=1000823253" alt="amazon-apps"/>
</map>



<map name="nav_imgmap_automotive" id="nav_imgmap_automotive">
<area shape="rect" coords="1,0,498,478" href="/b/ref=nav_flyout?_encoding=UTF8&node=4772060031" alt="auto-hp"/>
</map>



<map name="nav_imgmap_beauty-hpc" id="nav_imgmap_beauty-hpc">
<area shape="rect" coords="0,0,498,445" href="/s/ref=Dew?_encoding=UTF8&rh=i%3Abeauty%2Cn%3A6265207031" alt="beauty-hpc"/>
</map>



<map name="nav_imgmap_books" id="nav_imgmap_books">
<area shape="rect" coords="0,0,518,460" href="/dp/9385152149/ref=pop14" alt=""/>
</map>



<map name="nav_imgmap_cam-aud-vid" id="nav_imgmap_cam-aud-vid">
<area shape="rect" coords="0,0,485,470" href="/b/ref=cam-aud-vid?_encoding=UTF8&node=6477126031" alt=""/>
</map>



<map name="nav_imgmap_clothing-accessories" id="nav_imgmap_clothing-accessories">
<area shape="rect" coords="0,0,730,488" href="/b/ref=nav_m_designerstore?ie=UTF8&node=6153331031" alt="clothing-accessories"/>
</map>



<map name="nav_imgmap_clothing-shoes-luggage" id="nav_imgmap_clothing-shoes-luggage">
<area shape="rect" coords="62,266,482,486" href="/b/ref=nav_oct_flyout?_encoding=UTF8&node=6170563031" alt="Shop Now"/>
</map>



<map name="nav_imgmap_computer-accessories" id="nav_imgmap_computer-accessories">
<area shape="rect" coords="0,0,730,488" href="/dp/B00UYH9GZO/ref=nav-chromebook" alt="computers-accessories"/>
</map>



<map name="nav_imgmap_home-kitchen" id="nav_imgmap_home-kitchen">
<area shape="rect" coords="1,0,498,478" href="/s/rh=n%3A3474656031%2Cp_6%3AA3F20VPTXVFXW8%2Cp_89%3AKenstar%2Cn%3A1380263031%2Cn%3A%21976443031%2Cn%3A976442031&bbn=1380263031&rw_html_to_wsrp=1/ref=nav_flyout" alt="kenstar"/>
</map>



<map name="nav_imgmap_kindle" id="nav_imgmap_kindle">
<area shape="rect" coords="1,1,469,500" href="/dp/B00IOY5AS6/ref=nav_kindle voyage_text" alt="kindle"/>
</map>



<map name="nav_imgmap_phones-accessories" id="nav_imgmap_phones-accessories">
<area shape="rect" coords="0,0,493,475" href="/b/ref=nav_mob?_encoding=UTF8&node=1389401031" alt="phones-accessories"/>
</map>



<map name="nav_imgmap_shoes" id="nav_imgmap_shoes">
<area shape="rect" coords="0,0,459,486" href="/b/ref=nav_SM?ie=UTF8&node=6174654031" alt="shoes"/>
</map>



<map name="nav_imgmap_sports-outdoors" id="nav_imgmap_sports-outdoors">
<area shape="rect" coords="0,0,472,480" href="/b/ref=nav_SPORTS?_encoding=UTF8&node=4464985031" alt=" Minimum 60% OFF on Fan Merchandise"/>
</map>



<map name="nav_imgmap_toys-baby" id="nav_imgmap_toys-baby">
<area shape="rect" coords="0,0,518,460" href="/s/ref=nav_toysbaby?_encoding=UTF8&hidden-keywords=B00WK15ABQ%7C%20B00WK15MFA%7C%20B00WK15WZU%7C%20B00WK16CWM%7C%20B00WK16J84%7C%20B00K76RQUY%7C%20B00RLOXIY8%7C%20B00RLOZQIO%7C%20B00RN45KZG%7C%20B00LYWDKKU%7C%20B00RLP3Z36%7C%20B00AKBYN7A%7C%20B00AKBYN7U%7C%20B00AKU5YJM%7C%20B00IT7M1GW%7C%20B00J3QH9YM%7C%20B00DOPDNPM%7C%20B00AKBYOOC%7C&rh=i%3Atoys%2Cn%3A1350380031&rw_html_to_wsrp=1&sort=relevancerank" alt="shop-toys-ben10"/>
</map>



<map name="nav_imgmap_watches-jewelry" id="nav_imgmap_watches-jewelry">
<area shape="rect" coords="3,212,500,500" href="b/ref=?_encoding=UTF8&node=5328486031" alt=""/>
</map>




<script type="text/javascript"><!--



window.$Nav && $Nav.declare('config.navDebugHighres', false);


window.$Nav && $Nav.declare('config.upnavHighResImgInfo',
  {"upnav2xImageHeight":"","upnav2xImagePath":""});

window.$Nav && $Nav.declare('config.upnav2xAiryPreloadImgInfo',
  {"preloadImgPath":"","preloadImgHeight":""});

window.$Nav && $Nav.declare('config.upnav2xAiryPostSlateImgInfo',
  {"postslateImgHeight":"","postslateImgPath":""});

window.$Nav && $Nav.declare('config.pageType', 'Search');
window.$Nav && $Nav.declare('config.subPageType', '');

window.$Nav && $Nav.declare('config.dynamicMenuUrl', '/gp/navigation/ajax/dynamicmenu.html');

window.$Nav && $Nav.declare('config.dismissNotificationUrl',
  '/gp/navigation/ajax/dismissnotification.html');

window.$Nav && $Nav.declare('config.enableDynamicMenus', true);

window.$Nav && $Nav.declare('config.isInternal', false);

window.$Nav && $Nav.declare('config.isRecognized', false);

window.$Nav && $Nav.declare('config.transientFlyoutTrigger', '#nav-transient-flyout-trigger');

window.$Nav && $Nav.declare('config.subnavFlyoutUrl',
  '/gp/navigation/ajax/subnav-flyout');

window.$Nav && $Nav.declare('config.recordEvUrl',
  '/gp/navigation/ajax/recordevent.html');
window.$Nav && $Nav.declare('config.recordEvInterval', 15000);
window.$Nav && $Nav.declare('config.sessionId', '277-2541869-5922526');
window.$Nav && $Nav.declare('config.requestId', '0X849WPJZKXMCE756NPF');

window.$Nav && $Nav.declare('config.readyOnATF', true);

window.$Nav && $Nav.declare('config.dynamicMenuArgs',
  {"rid":"0X849WPJZKXMCE756NPF","isPrime":0,"weblabs":"","primeMenuWidth":310});

window.$Nav && $Nav.declare('config.signOutText',
  null);

window.$Nav && $Nav.declare('config.yourAccountPrimeURL',
  null);

window.$Nav && $Nav.declare('config.yourAccountPrimeHover',
  false);

window.$Nav && $Nav.declare('config.searchBackState',
  {"suppressNoCache":null,"searchbar":{"data":{"nav-metadata":{"digest":"j6hJTM0VLm6q5VrT9gU97rVLmvg","selected":0},"options":[{"_display":"All Departments","value":"search-alias=aps","selected":"selected"},{"_display":"Baby","value":"search-alias=baby"},{"_display":"Beauty","value":"search-alias=beauty"},{"_display":"Books","value":"search-alias=stripbooks"},{"_display":"Car & Motorbike","value":"search-alias=automotive"},{"_display":"Clothing & Accessories","value":"search-alias=apparel"},{"_display":"Computers & Accessories","value":"search-alias=computers"},{"_display":"Electronics","value":"search-alias=electronics"},{"_display":"Gift Cards","value":"search-alias=gift-cards"},{"_display":"Gourmet & Specialty Foods","value":"search-alias=grocery"},{"_display":"Health & Personal Care","value":"search-alias=hpc"},{"_display":"Home & Kitchen","value":"search-alias=kitchen"},{"_display":"Jewellery","value":"search-alias=jewelry"},{"_display":"Kindle Store","value":"search-alias=digital-text"},{"_display":"KiranaNow","value":"search-alias=everyday-essentials"},{"_display":"Luggage & Bags","value":"search-alias=luggage"},{"_display":"Movies & TV Shows","value":"search-alias=dvd"},{"_display":"Music","value":"search-alias=popular"},{"_display":"Musical Instruments","value":"search-alias=mi"},{"_display":"Office Products","value":"search-alias=office-products"},{"_display":"Pet Supplies","value":"search-alias=pets"},{"_display":"Shoes & Handbags","value":"search-alias=shoes"},{"_display":"Software","value":"search-alias=software"},{"_display":"Sports, Fitness & Outdoors","value":"search-alias=sporting"},{"_display":"Toys & Games","value":"search-alias=toys"},{"_display":"Video Games","value":"search-alias=videogames"},{"_display":"Watches","value":"search-alias=watches"}]},"type":"searchbar"},"catsubnav":{"digest":"0","type":"html","data":""}});










if (window.amznJQ && amznJQ.available) {
  amznJQ.available('jQuery', function() {
    if (!jQuery.isArray) {
      jQuery.isArray = function(o) {
        return Object.prototype.toString.call(o) === "[object Array]";
      };
    }
  });
}


    if (typeof uet == 'function') {
      uet('bb', 'iss-init-pc', {wb: 1});
    }

    if (!window.$SearchJS && window.$Nav) {
      window.$SearchJS = $Nav.make('sx');
    }


  var opts = {
      host: "completion.amazon.co.uk/search/complete"
    , marketId: "44571"
    , obfuscatedMarketId: "A21TJRUUN4KGV"
    , searchAliases: ["aps", "stripbooks", "computers", "digital-text", "dvd", "electronics", "hpc", "kitchen", "popular", "software", "videogames", "toys", "beauty", "baby", "watches", "jewelry", "luggage", "mobile-apps", "apparel", "shoes", "sporting", "gift-cards", "grocery", "mi", "office-products", "pets", "automotive"]
    , isDoCtw: 0
    , pageType: "Search"
    , requestId: "0X849WPJZKXMCE756NPF"
    , keydownTriggeredWeblabs: []
    , displayTriggeredWeblabs: []
    , isDdInT3: 0
    , isDdInT1: 0
    , isJpOrCn: 0
    , isUseAuiIss: 1
  };

  var issOpts = {
      fallbackFlag: 1
    , isDigitalFeaturesEnabled: 0
    , isWayfindingEnabled: 0
    , dropdown: "select.searchSelect"
    , departmentText: "in {department}"
    , suggestionText: "Search suggestions"
    , issCorpusSuggestionText: ""
    , isTriggerIssOnClick: 0
    , imeEnh: 0
    , xcatSuggestionImprovementFlag: 2
    , np: 0
    , issCorpus: []
    , cf: 0
  };


  if (opts.isUseAuiIss === 1) {
    $Nav.when('sx.iss').run('iss-mason-init', function(iss){
      var issInitObj = buildIssInitObject(opts, issOpts, true);
      new iss.IssParentCoordinator(issInitObj);

      tryInitClientTriggeredWeblabs(issInitObj);
    });
  } else if (window.$SearchJS) {

    var iss;

    // BEGIN Deprecated globals
    var issHost = opts.host
      , issMktid = opts.marketId
      , issSearchAliases = opts.searchAliases
      , updateISSCompletion = function() { iss.updateAutoCompletion(); };
    // END deprecated globals




    $SearchJS.when('jQuery', 'search-js-autocomplete-lib').run('autocomplete-init', initializeAutocomplete);
    $SearchJS.when('canCreateAutocomplete').run('createAutocomplete', createAutocomplete);


    if (opts.isDdInT3) {
      $SearchJS.when('search-js-autocomplete').run('autocomplete-dd-init', function(){ mergeBTFDropdown(); });
    }

    if (opts.isDdInT1) {
      $SearchJS.when('search-js-autocomplete').run('autocomplete-dd-init', function(){ searchDropdown(); });
    }

  } // END conditional for window.$SearchJS



  function initializeAutocomplete(jQuery) {

    var issInitObj = buildIssInitObject(opts, issOpts);

    tryInitClientTriggeredWeblabs(issInitObj);
  } // END initializeAutocomplete



  function tryInitClientTriggeredWeblabs(issInitObj) {

    if (opts.isDoCtw) {
      $SearchJS.importEvent('search-csl');
      $SearchJS.when('search-csl').run('autocomplete-csl-init', function delegateToInitSearchCsl(searchCSL) { initSearchCsl( searchCSL, issInitObj ); } );
    } else {
      $SearchJS.declare('canCreateAutocomplete', issInitObj);
    }
  }



  function initSearchCsl(searchCSL, issInitObject) {
    searchCSL.init(opts.pageType, (window.ue && window.ue.rid) || opts.requestId);


    var keydownCtw = opts.keydownTriggeredWeblabs;
    var displayCtw = opts.displayTriggeredWeblabs;


    issInitObject.doCTWKeydown = function(e) {
        for (var i = 0; i < keydownCtw.length; i++) {
          searchCSL.addWlt(keydownCtw[i].call ? keydownCtw[i](e) : keydownCtw[i]);
        }
      };

    issInitObject.doCTWDisplay = function() {
        for (var i = 0; i < displayCtw.length; i++) {
          searchCSL.addWlt(displayCtw[i].call ? displayCtw[i]() : displayCtw[i]);
        }
      };

    $SearchJS.declare('canCreateAutocomplete', issInitObject);
  } // END initSearchCsl



  function createAutocomplete(issObject) {
    iss = new AutoComplete(issObject);

    $SearchJS.publish('search-js-autocomplete', iss);

    logMetrics();
  } // END createAutocomplete



  function buildIssInitObject(opts, issOpts, isNewIss) {
    var issInitObj = {
        src: opts.host
      , mkt: opts.marketId
      , obfMkt: opts.obfuscatedMarketId
      , aliases: opts.searchAliases
      , fb: issOpts.fallbackFlag
      , isDigitalFeaturesEnabled: issOpts.isDigitalFeaturesEnabled
      , isWayfindingEnabled: issOpts.isWayfindingEnabled
      , deptText: issOpts.departmentText
      , sugText: issOpts.suggestionText
      , issCorpusSugText: issOpts.issCorpusSuggestionText
      , ime: opts.isJpOrCn
      , mktid: opts.marketId
      , qs: opts.isJpOrCn
      , issCorpus: issOpts.issCorpus
      , deepNodeISS: {
          searchAliasAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAlias()) ||
                   jQuery('select.searchSelect').children().attr('data-root-alias');
          },
          searchAliasDisplayNameAccessor: function() {
            return (window.SearchPageAccess && window.SearchPageAccess.searchAliasDisplayName());
          }
        }
    };

    // If we aren't using the new ISS then we need to add these properties
    if (!isNewIss) {
      issInitObj.dd = issOpts.dropdown; // The element with id searchDropdownBox doesn't exist in C.
      issInitObj.imeEnh = issOpts.imeEnh;
      issInitObj.imeSpacing = issOpts.imeSpacing;
      issInitObj.xcatSuggestionImprovementFlag = issOpts.xcatSuggestionImprovementFlag;
      issInitObj.isNavInline = 1;
      issInitObj.triggerISSOnClick = issOpts.triggerIssOnClick
      issInitObj.sc = 1;
      issInitObj.np = issOpts.np;
    }

    return issInitObj;
  } // END buildIssInitObject


  function logMetrics() {
    if (typeof uet == 'function' && typeof uex == 'function' ) {
      uet('be', 'iss-init-pc', {wb: 1});
      uex('ld', 'iss-init-pc', {wb: 1});
    }
  } // END logMetrics



    window.amznJQ && amznJQ.declareAvailable('navbarInline');
    window.$Nav && $Nav.declare('nav.inline');

    window.amznJQ && amznJQ.available('jQuery', function() {
        amznJQ.available('navbarJS-beacon', function(){});
    });

(function (i) {
i.onload = function() {window.uet && uet('ne')};
i.src = window._navbarSpriteUrl;
}(new Image()));

window.$Nav && $Nav.declare('config.autoFocus', false);


window.$Nav && $Nav.declare('config.responsiveTouchAgents', ["ieTouch"]);

window.$Nav && $Nav.declare('config.responsiveGW',false);

window.$Nav && $Nav.declare('config.velocityFlyoutToggling', false);
window.$Nav && $Nav.declare('config.velocityFlyoutThreshold', 40);

window.$Nav && $Nav.declare('config.twoClickFlyouts',false);

window.$Nav && $Nav.declare('config.pageHideEnabled',false);

window.$Nav && $Nav.declare('config.sslTriggerType','');
window.$Nav && $Nav.declare('config.sslTriggerRetry',0);

window.$Nav && $Nav.declare('config.bletchley', false);

window.$Nav && $Nav.declare('config.doubleCart',false);


window.$Nav && $Nav.declare('config.fixedBarBeacon',true);

window.$Nav && $Nav.declare('config.signInOverride', false);

window.$Nav && $Nav.declare('config.signInTooltip',true);


window.$Nav && $Nav.declare('config.isPrimeMember',false);

window.$Nav && $Nav.declare('config.primeTooltip',false);

window.$Nav && $Nav.declare('config.carnac',false);

window.$Nav && $Nav.declare('config.csYourAccount',false);

window.$Nav && $Nav.declare('config.cartFlyoutDisabled', false);


window.$Nav && $Nav.declare('config.ewc',false);


window.$Nav && $Nav.declare('config.blackbelt', false);
window.$Nav && $Nav.declare('config.beaconbelt', false);

window.$Nav && $Nav.declare('config.searchapiEndpoint',false);

    window._navbar = window._navbar || {};
    window._navbar.browsepromos = window._navbar.browsepromos || {};

 _navbar.browsepromos['amazon-apps'] = {"width":519,"promoType":"wide","vertOffset":"-9","horizOffset":"-20","height":495,"image":"http://g-ecx.images-amazon.com/images/G/31/img13/mshop/sweep23/Samsung-S6_Flyout_normal._V306102577_.png"};
 _navbar.browsepromos['automotive'] = {"width":518,"promoType":"wide","vertOffset":"-10","horizOffset":"-20","height":460,"image":"http://g-ecx.images-amazon.com/images/G/31/img14/automotive/launch/Auto_Flyout_518X460_V3.0._V328293334_.png"};
 _navbar.browsepromos['beauty-hpc'] = {"width":520,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":495,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Beauty/Luxury/ForestEssentials/Final/ForestEssentials_Flyout_520x495._V306568968_.png"};
 _navbar.browsepromos['books'] = {"width":500,"promoType":"wide","vertOffset":"-10","horizOffset":"-10","height":500,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/books/032015/amish/500x500Flyout_edit05_refresh_Small._V304605749_.png"};
 _navbar.browsepromos['cam-aud-vid'] = {"width":498,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":485,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Audio-Video/PhilipsSports/Philips-Sports-Headphones-Flyout-Normal-V2._V307211132_.png"};
 _navbar.browsepromos['clothing-accessories'] = {"width":500,"promoType":"wide","vertOffset":"0","horizOffset":"-25","height":500,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/softlines-stores/Arrow/offer/ARROW-2Col._V306114550_.png"};
 _navbar.browsepromos['clothing-shoes-luggage'] = {"width":482,"promoType":"wide","vertOffset":"-5","horizOffset":"-10","height":486,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Luggage/March/BTS/BTS_Flyout._V310274118_.png"};
 _navbar.browsepromos['computer-accessories'] = {"width":519,"promoType":"wide","vertOffset":"00","horizOffset":"-21","height":479,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/PC/May/Chromebook/Chromebook-Flyout._V304605380_.png"};
 _navbar.browsepromos['home-kitchen'] = {"width":519,"promoType":"wide","vertOffset":"-10","horizOffset":"-20","height":495,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/home/brand/kenstar/kenstarflyout28thmar._V307258046_.png"};
 _navbar.browsepromos['kindle'] = {"width":500,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":469,"image":"http://g-ecx.images-amazon.com/images/G/31/kindle/merch/2015/Device/Icewine/Kindle-Voyage_500x469_flyout._V308433019_.jpg"};
 _navbar.browsepromos['phones-accessories'] = {"width":499,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":483,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Mobiles/ART/Upto40_Normal_Flyout._V305838270_.png"};
 _navbar.browsepromos['shoes'] = {"width":500,"promoType":"wide","vertOffset":"-12","horizOffset":"-12","height":510,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/softlines-stores/Reebok/Flyout460X486-Skechers._V310234533_.gif"};
 _navbar.browsepromos['sports-outdoors'] = {"width":500,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":500,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Sports/IPL2015/WinWin/16th/version-1/500x500Flyout-7Pm._V304579047_.png"};
 _navbar.browsepromos['toys-baby'] = {"width":499,"promoType":"wide","vertOffset":"0","horizOffset":"0","height":497,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/Toys/ART/Ben-10/2-Colum_Flyout._V305894877_.png"};
 _navbar.browsepromos['watches-jewelry'] = {"width":500,"promoType":"wide","vertOffset":"-10","horizOffset":"-10","height":500,"image":"http://g-ecx.images-amazon.com/images/G/31/img15/jewellery/201504/April_Flip/Final/Precious-Gemstones-2-col._V306471187_.png"};


    window.$Nav && $Nav.declare('config.browsePromos', window._navbar.browsepromos);


window.$Nav && $Nav.declare('config.extendedFlyout', false);

window.$Nav && $Nav.declare('config.enableBbPrefetch', false);

window.$Nav && $Nav.declare('config.enableBbAaProx', false);

window.$Nav && $Nav.declare('configComplete');

--></script>

<!--Tilu -->




<div id="main" class="nav_redesign s-left-nav-rib-redesign s-span-page" data-page-construction="auisearch">
            <div id="topStatic">
                <script type="text/javascript">

    function addCSSRule(selector, rule) {
        var isMsie = (/msie/.test(navigator.userAgent.toLowerCase()));

        var styleTag = document.createElement("style");
        styleTag.setAttribute("type", "text/css");
        styleTag.setAttribute("id", "hideResults");

        if (!isMsie) {
            styleTag.appendChild(document.createTextNode(selector + " {" + rule + "}"));
        }

        document.getElementsByTagName("head")[0].appendChild(styleTag);

        if (isMsie && document.styleSheets && document.styleSheets.length > 0) {
            var lastStyleTag = document.styleSheets[document.styleSheets.length - 1];
            var selectors = selector.split(',');
            for(var i = 0; i < selectors.length; i++){
                lastStyleTag.addRule(selectors[i], rule);
            }
        }
    };



    if (!window.sxaj && location.hash && location.hash != '#') {

        var sbox = document.getElementById("twotabsearchtextbox");
        if (sbox) {
            sbox.setAttribute("value", "");
        }


        addCSSRule("#center,#centerBelow,#centerBelowExtra,#footer", "display: none");
        addCSSRule("#leftNav,#top", "visibility: hidden");


        window.slDisabled = 1;
    }

    function viewCompleteImageLoaded(image, time, resultCount, shouldUseCSMScopes) {
         amzn.sx.utils.jsDepMgr.when('clickToViewLogger', 'viewCompleteImageLoaded',
           function(clickToViewLogger) {
            if (typeof ctvcL == 'undefined') {ctvcL = new clickToViewLogger.ClickToViewCompleteLogger("false");}
            ctvcL.iL(image, time, resultCount, shouldUseCSMScopes);
           }
         );
    };
</script>
</div>

            <div id="top">
                <div id="results-atf-images-preload" style="display:none;">
    <img src="http://ecx.images-amazon.com/images/I/410jtII-TxL._AA160_.jpg" />
        <img src="http://ecx.images-amazon.com/images/I/41eSh%2BZT8IL._AA160_.jpg" />
        <img src="http://ecx.images-amazon.com/images/I/51it-YPHAdL._AA160_.jpg" />
        <img src="http://ecx.images-amazon.com/images/I/41oNrpQ2USL._AA160_.jpg" />
        </div>
</div>

            <div id="topAmabot">
                </div>

            <div id="searchTemplate" class="searchTemplate listLayout so_in_en" >
                <div id="topDynamicContent">
                    <div id="s-result-info-bar" class="a-row a-spacing-base searchUndoAUIHacks"><div id="s-result-info-bar-content" class="a-row"><div class="a-column a-span8 a-spacing-none"><div class="s-first-column">
            <h2 id="s-result-count" class="a-size-base a-spacing-small a-spacing-top-small a-text-normal">1-16 of 12,335 results for <span><span class="a-color-state a-text-bold">&#034;smartphones&#034;</span></span></h2></div>
        </div><div class="a-column a-span4 a-text-right a-spacing-none a-span-last"><div class="a-row a-spacing-micro a-spacing-top-micro"><div class="s-last-column">
                    <div class="a-popover-preload" id="a-popover-department-picker"><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_0?fst=as%3Aoff&amp;rh=n%3A976419031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Electronics</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_11?fst=as%3Aoff&amp;rh=n%3A976392031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Computers &amp; Accessories</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_21?fst=as%3Aoff&amp;rh=n%3A1350380031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Toys &amp; Games</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_24?fst=as%3Aoff&amp;rh=n%3A976389031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Books</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_30?fst=as%3Aoff&amp;rh=n%3A1350387031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Watches</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_32?rh=k%3Asmartphones%2Ci%3Amisc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Everything Else</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_33?rh=k%3Asmartphones%2Ci%3Adigital-text&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Kindle Store</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_34?rh=k%3Asmartphones%2Ci%3Aautomotive&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Car &amp; Motorbike</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_35?rh=k%3Asmartphones%2Ci%3Asporting&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Sports, Fitness &amp; Outdoors</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_36?rh=k%3Asmartphones%2Ci%3Akitchen&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Home &amp; Kitchen</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_37?rh=k%3Asmartphones%2Ci%3Ababy&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Baby</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_38?rh=k%3Asmartphones%2Ci%3Ahpc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Health &amp; Personal Care</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_39?rh=k%3Asmartphones%2Ci%3Ami&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Musical Instruments</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_40?rh=k%3Asmartphones%2Ci%3Aoffice-products&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Office Products</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_41?rh=k%3Asmartphones%2Ci%3Aluggage&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Luggage &amp; Bags</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_42?rh=k%3Asmartphones%2Ci%3Avideogames&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Video Games</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_43?rh=k%3Asmartphones%2Ci%3Asoftware&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Software</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_44?rh=k%3Asmartphones%2Ci%3Aapparel&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Clothing &amp; Accessories</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_45?rh=k%3Asmartphones%2Ci%3Ashoes&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Shoes &amp; Handbags</a></div></div><span class="s-inline-block a-spacing-mini a-spacing-top-mini">
        <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;name&quot;:&quot;department-picker&quot;,&quot;closeButton&quot;:false}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><span class="a-size-base a-color-base">Choose a Department to sort</span><i class="a-icon a-icon-popover"></i></a></span></span>
</div>
            </div></div></div></div></div>
                <div id="rightContainerATF">
                        <div id="rightResultsATF">
                            <div id="widthPreserver"></div>

                        <div id="center">
                                <div class="sx-sparkle-container s-box">
  <a href="http://www.amazon.in/s?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_89%3AIntex%2Cp_76%3A1318482031%2Cn%3A!976420031&bbn=1389432031&ie=UTF8&ref=spks_0_0_623865987&pf_rd_p=623865987&pf_rd_m=A21TJRUUN4KGV&pf_rd_t=301&pf_rd_s=desktop-auto-sparkle&pf_rd_r=0X849WPJZKXMCE756NPF&pf_rd_i=smartphones&qid=1431746869" class="sx-block a-link-normal a-text-normal">
    <img class="sx-sparkle-left sx-sparkle-image-medium" src="http://g-ecx.images-amazon.com/images/G/31/ui/loadIndicators/loading-large_labeled._V147965460_UY80_.gif">
    <div class="sx-sparkle-right sx-sparkle-text">
      <span class="sx-sparkle-title-primary">Wide range of popular Intex Mobiles</span>
      <div class="sx-sparkle-title-secondary">Shop now</div>
    </div>
  </a>
</div>
<div class="a-row a-spacing-mini"><span class="a-size-base a-color-base">Related Searches:<span class="a-letter-space"></span><span class="a-size-base a-color-base"><a class="a-link-normal a-text-normal" href="/s/ref=sr_kk_1?rh=i%3Aaps%2Ck%3Asamsung+smartphones&amp;keywords=samsung+smartphones&amp;ie=UTF8&amp;qid=1431746869">samsung smartphones</a></span><span class="a-size-base a-color-base">, <a class="a-link-normal a-text-normal" href="/s/ref=sr_kk_2?rh=i%3Aaps%2Ck%3Asmart+phones&amp;keywords=smart+phones&amp;ie=UTF8&amp;qid=1431746869">smart phones</a></span><span class="a-size-base a-color-base">, <a class="a-link-normal a-text-normal" href="/s/ref=sr_kk_3?rh=i%3Aaps%2Ck%3Asmartphones+android&amp;keywords=smartphones+android&amp;ie=UTF8&amp;qid=1431746869">smartphones android</a>.</span></span></div><div id="atfResults" class="a-row s-result-list-parent-container"><ul id="s-results-list-atf" class="s-result-list s-col-1 s-col-ws-1 s-result-list-hgrid s-height-equalized s-list-view s-text-condensed"><li id="result_0" data-asin="B00VEB055E" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-2-White/dp/B00VEB055E/ref=sr_1_1?ie=UTF8&amp;qid=1431746869&amp;sr=8-1&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/410jtII-TxL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Redmi 2 (White)" href="http://www.amazon.in/Mi-Redmi-2-White/dp/B00VEB055E/ref=sr_1_1?ie=UTF8&amp;qid=1431746869&amp;sr=8-1&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Redmi 2 (White)</h2></a><span class="a-letter-space"></span><span class="a-letter-space"></span><span class="a-size-small a-color-secondary">15 March 2015</span><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Mi</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-2-White/dp/B00VEB055E/ref=sr_1_1?ie=UTF8&amp;qid=1431746869&amp;sr=8-1&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>6,999.00</span></a><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00VEB055E/ref=sr_1_1_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-1&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>2 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>6,999.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00VEB055E">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00VEB055E&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4.1 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-2-White/dp/B00VEB055E/ref=sr_1_1?ie=UTF8&amp;qid=1431746869&amp;sr=8-1&amp;keywords=smartphones#customerReviews">378</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_1?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_1" data-asin="B00I060SSA" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Champange/dp/B00I060SSA/ref=sr_1_2?ie=UTF8&amp;qid=1431746869&amp;sr=8-2&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41eSh%2BZT8IL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Bolt A24 (Champange)" href="http://www.amazon.in/Micromax-Bolt-A24-Champange/dp/B00I060SSA/ref=sr_1_2?ie=UTF8&amp;qid=1431746869&amp;sr=8-2&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Bolt A24 (Champange)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Champange/dp/B00I060SSA/ref=sr_1_2?ie=UTF8&amp;qid=1431746869&amp;sr=8-2&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>2,298.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>3,750.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>1,452.00
        (39%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00I060SSA/ref=sr_1_2_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-2&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>7 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>2,271.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00I060SSA">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00I060SSA&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-3"><span class="a-icon-alt">3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Champange/dp/B00I060SSA/ref=sr_1_2?ie=UTF8&amp;qid=1431746869&amp;sr=8-2&amp;keywords=smartphones#customerReviews">16</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_2?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_2" data-asin="B00GC441U8" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A369i-Black/dp/B00GC441U8/ref=sr_1_3?ie=UTF8&amp;qid=1431746869&amp;sr=8-3&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/51it-YPHAdL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Lenovo A369i (Black)" href="http://www.amazon.in/Lenovo-A369i-Black/dp/B00GC441U8/ref=sr_1_3?ie=UTF8&amp;qid=1431746869&amp;sr=8-3&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Lenovo A369i (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Lenovo</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A369i-Black/dp/B00GC441U8/ref=sr_1_3?ie=UTF8&amp;qid=1431746869&amp;sr=8-3&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>3,770.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>6,999.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>3,229.00
        (46%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00GC441U8/ref=sr_1_3_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-3&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>3 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>3,770.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00GC441U8">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00GC441U8&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A369i-Black/dp/B00GC441U8/ref=sr_1_3?ie=UTF8&amp;qid=1431746869&amp;sr=8-3&amp;keywords=smartphones#customerReviews">719</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_3?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_3" data-asin="B00Q2HGF3Q" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Microsoft-Lumia-535-Black-Dual/dp/B00Q2HGF3Q/ref=sr_1_4?ie=UTF8&amp;qid=1431746869&amp;sr=8-4&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41oNrpQ2USL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);if (typeof uet =='function') { uet('af'); if(window.amzn && amzn.sx && amzn.sx.utils && amzn.sx.utils.jsDepMgr) {amzn.sx.utils.jsDepMgr.when('jQuery','ajax_ue_init_manageLoad', function($) { var u=$.searchUE;if(u) {u.manageLoad();}});} } if(window.amzn && amzn.sx && amzn.sx.utils && amzn.sx.utils.jsDepMgr) {amzn.sx.utils.jsDepMgr.when('search-js-general','atf_event_trigger', function() {SPUtils.triggerATFEvent(0);});}" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Microsoft Lumia 535 (Black, Dual SIM)" href="http://www.amazon.in/Microsoft-Lumia-535-Black-Dual/dp/B00Q2HGF3Q/ref=sr_1_4?ie=UTF8&amp;qid=1431746869&amp;sr=8-4&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Microsoft Lumia 535 (Black, Dual SIM)</h2></a><span class="a-letter-space"></span><span class="a-letter-space"></span><span class="a-size-small a-color-secondary">10 December 2014</span><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Microsoft</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Microsoft-Lumia-535-Black-Dual/dp/B00Q2HGF3Q/ref=sr_1_4?ie=UTF8&amp;qid=1431746869&amp;sr=8-4&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>7,137.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>8,699.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>1,562.00
        (18%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00Q2HGF3Q/ref=sr_1_4_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-4&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>41 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>7,137.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00Q2HGF3Q">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00Q2HGF3Q&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-3-5"><span class="a-icon-alt">3.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Microsoft-Lumia-535-Black-Dual/dp/B00Q2HGF3Q/ref=sr_1_4?ie=UTF8&amp;qid=1431746869&amp;sr=8-4&amp;keywords=smartphones#customerReviews">691</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_4?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li></ul></div></div>

                            <div id="centerBelow">
                                <div id="search-js-btf">

  <script type="text/javascript">

      amzn.sx.utils.jsDepMgr.when('jQuery search-js-general breadcrumb', 'searchJsBtf', function($, searchComponents, breadcrumb) {

          SPUtils.triggerEvent("spFold");


          breadcrumb.breadcrumbSearch();


          breadcrumb.editableBreadcrumb();


          $(function () {searchComponents.hoverOverImageTriggersTitleHover();});

          SPUtils.afterEvent("spATFEvent", function () {

            registerAivHandler("atf");


              setFinancialValidation();
          });


          if (typeof processBundlesFlyouts == 'function') {
              processBundlesFlyouts('atf');
          }


                      amzn.sx.utils.jsDepMgr.when('popover', 'promotionPopover', function() {
                          processPromotionsPopover();
                      });


      });

      </script>

</div>
<div id="raw-search-js-btf" class="searchUndoAUIHacks">



















<div id="search-js-btf-external">









<script language="javascript">var cloudfrontImg = new Image();if (location.protocol == "http:") {if (window.addEventListener) {window.addEventListener("load", function() {setTimeout(function(){ cloudfrontImg.src = "http://cloudfront-labs.amazonaws.com/x.png"; }, 400);}, false);} else if (window.attachEvent) {window.attachEvent("onload", function() {setTimeout(function(){ cloudfrontImg.src = "http://cloudfront-labs.amazonaws.com/x.png"; }, 400);});}} </script>






</div>



</div><div id="btfResults" class="a-row s-result-list-parent-container"><ul class="s-result-list s-col-1 s-col-ws-1 s-result-list-hgrid s-height-equalized s-list-view s-text-condensed"><li id="result_4" data-asin="B00KLU9X98" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Unite-A106-White-8GB/dp/B00KLU9X98/ref=sr_1_5?ie=UTF8&amp;qid=1431746869&amp;sr=8-5&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41HUzGt8PBL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Unite 2 A106 (White, 8GB)" href="http://www.amazon.in/Micromax-Unite-A106-White-8GB/dp/B00KLU9X98/ref=sr_1_5?ie=UTF8&amp;qid=1431746869&amp;sr=8-5&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Unite 2 A106 (White, 8GB)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Unite-A106-White-8GB/dp/B00KLU9X98/ref=sr_1_5?ie=UTF8&amp;qid=1431746869&amp;sr=8-5&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>5,205.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>8,499.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>3,294.00
        (39%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00KLU9X98/ref=sr_1_5_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-5&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>23 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>5,194.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00KLU9X98">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00KLU9X98&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Unite-A106-White-8GB/dp/B00KLU9X98/ref=sr_1_5?ie=UTF8&amp;qid=1431746869&amp;sr=8-5&amp;keywords=smartphones#customerReviews">1,971</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_5?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_5" data-asin="B00NLB9P1U" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-White/dp/B00NLB9P1U/ref=sr_1_6?ie=UTF8&amp;qid=1431746869&amp;sr=8-6&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/51YoLq21-xL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Lenovo A536 (White)" href="http://www.amazon.in/Lenovo-A536-White/dp/B00NLB9P1U/ref=sr_1_6?ie=UTF8&amp;qid=1431746869&amp;sr=8-6&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Lenovo A536 (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Lenovo</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-White/dp/B00NLB9P1U/ref=sr_1_6?ie=UTF8&amp;qid=1431746869&amp;sr=8-6&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>7,500.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>10,999.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>3,499.00
        (32%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00NLB9P1U/ref=sr_1_6_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-6&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>8 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>6,600.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00NLB9P1U">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00NLB9P1U&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-White/dp/B00NLB9P1U/ref=sr_1_6?ie=UTF8&amp;qid=1431746869&amp;sr=8-6&amp;keywords=smartphones#customerReviews">516</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_6?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_6" data-asin="B00KTC2PAW" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Black/dp/B00KTC2PAW/ref=sr_1_7?ie=UTF8&amp;qid=1431746869&amp;sr=8-7&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41NUL1SSqVL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Bolt A24 (Black)" href="http://www.amazon.in/Micromax-Bolt-A24-Black/dp/B00KTC2PAW/ref=sr_1_7?ie=UTF8&amp;qid=1431746869&amp;sr=8-7&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Bolt A24 (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Black/dp/B00KTC2PAW/ref=sr_1_7?ie=UTF8&amp;qid=1431746869&amp;sr=8-7&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>2,280.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>3,750.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>1,470.00
        (39%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-price">Only 1 left in stock - order soon.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00KTC2PAW/ref=sr_1_7_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-7&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>7 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>2,100.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00KTC2PAW">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00KTC2PAW&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-3-5"><span class="a-icon-alt">3.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A24-Black/dp/B00KTC2PAW/ref=sr_1_7?ie=UTF8&amp;qid=1431746869&amp;sr=8-7&amp;keywords=smartphones#customerReviews">8</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_7?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_7" data-asin="B00N4QFUAM" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-Black/dp/B00N4QFUAM/ref=sr_1_8?ie=UTF8&amp;qid=1431746869&amp;sr=8-8&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/51-txpPSZYL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Lenovo A536 (Black)" href="http://www.amazon.in/Lenovo-A536-Black/dp/B00N4QFUAM/ref=sr_1_8?ie=UTF8&amp;qid=1431746869&amp;sr=8-8&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Lenovo A536 (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Lenovo</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-Black/dp/B00N4QFUAM/ref=sr_1_8?ie=UTF8&amp;qid=1431746869&amp;sr=8-8&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>10,999.00</span></a><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00N4QFUAM/ref=sr_1_8_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-8&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>7 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>6,600.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00N4QFUAM">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00N4QFUAM&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-A536-Black/dp/B00N4QFUAM/ref=sr_1_8?ie=UTF8&amp;qid=1431746869&amp;sr=8-8&amp;keywords=smartphones#customerReviews">516</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_8?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_8" data-asin="B00MA9X3JO" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Spice-Android-battery-1-3ghzdual-Silver/dp/B00MA9X3JO/ref=sr_1_9?ie=UTF8&amp;qid=1431746869&amp;sr=8-9&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41bWFJLRZ%2BL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Spice FLO 359,Android KIT KAAT 4.4&quot;,1400 mAh battery,2MP back cam,1.3ghzdual (Silver)" href="http://www.amazon.in/Spice-Android-battery-1-3ghzdual-Silver/dp/B00MA9X3JO/ref=sr_1_9?ie=UTF8&amp;qid=1431746869&amp;sr=8-9&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Spice FLO 359,Android KIT KAAT 4.4&quot;,1400 mAh battery,2MP back cam,1.3ghzdual (Silver)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Spice</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Spice-Android-battery-1-3ghzdual-Silver/dp/B00MA9X3JO/ref=sr_1_9?ie=UTF8&amp;qid=1431746869&amp;sr=8-9&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>2,899.00</span></a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00MA9X3JO/ref=sr_1_9_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-9&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>5 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>2,850.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00MA9X3JO">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00MA9X3JO&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Spice-Android-battery-1-3ghzdual-Silver/dp/B00MA9X3JO/ref=sr_1_9?ie=UTF8&amp;qid=1431746869&amp;sr=8-9&amp;keywords=smartphones#customerReviews">8</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_9?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_9" data-asin="B00IXCZEEE" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Power-A96-Black/dp/B00IXCZEEE/ref=sr_1_10?ie=UTF8&amp;qid=1431746869&amp;sr=8-10&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41H7L4Am5XL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Canvas Power A96 (Black)" href="http://www.amazon.in/Micromax-Canvas-Power-A96-Black/dp/B00IXCZEEE/ref=sr_1_10?ie=UTF8&amp;qid=1431746869&amp;sr=8-10&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Canvas Power A96 (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Power-A96-Black/dp/B00IXCZEEE/ref=sr_1_10?ie=UTF8&amp;qid=1431746869&amp;sr=8-10&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>7,999.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>12,999.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>5,000.00
        (38%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-price">Only 1 left in stock - order soon.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00IXCZEEE/ref=sr_1_10_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-10&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>4 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>6,390.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00IXCZEEE">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00IXCZEEE&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-3"><span class="a-icon-alt">3.1 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Power-A96-Black/dp/B00IXCZEEE/ref=sr_1_10?ie=UTF8&amp;qid=1431746869&amp;sr=8-10&amp;keywords=smartphones#customerReviews">472</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_10?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_10" data-asin="B00OTI5DOW" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-A064-Bolt-White/dp/B00OTI5DOW/ref=sr_1_11?ie=UTF8&amp;qid=1431746869&amp;sr=8-11&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/11mvFlQsfQL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Bolt A064 (White)" href="http://www.amazon.in/Micromax-A064-Bolt-White/dp/B00OTI5DOW/ref=sr_1_11?ie=UTF8&amp;qid=1431746869&amp;sr=8-11&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Bolt A064 (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-A064-Bolt-White/dp/B00OTI5DOW/ref=sr_1_11?ie=UTF8&amp;qid=1431746869&amp;sr=8-11&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>3,249.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>4,499.00</span></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>1,250.00
        (28%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00OTI5DOW/ref=sr_1_11_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-11&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>3 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>3,090.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00OTI5DOW">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00OTI5DOW&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-A064-Bolt-White/dp/B00OTI5DOW/ref=sr_1_11?ie=UTF8&amp;qid=1431746869&amp;sr=8-11&amp;keywords=smartphones#customerReviews">46</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_11?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_11" data-asin="B00PQHZ4CQ" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Panasonic-Eluga-S-Black/dp/B00PQHZ4CQ/ref=sr_1_12?ie=UTF8&amp;qid=1431746869&amp;sr=8-12&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41x%2B7E4SjdL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Panasonic Eluga S (Black)" href="http://www.amazon.in/Panasonic-Eluga-S-Black/dp/B00PQHZ4CQ/ref=sr_1_12?ie=UTF8&amp;qid=1431746869&amp;sr=8-12&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Panasonic Eluga S (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Panasonic</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Panasonic-Eluga-S-Black/dp/B00PQHZ4CQ/ref=sr_1_12?ie=UTF8&amp;qid=1431746869&amp;sr=8-12&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>9,685.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>13,990.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>4,305.00
        (31%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00PQHZ4CQ/ref=sr_1_12_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-12&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>9 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>9,685.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00PQHZ4CQ">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00PQHZ4CQ&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4.1 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Panasonic-Eluga-S-Black/dp/B00PQHZ4CQ/ref=sr_1_12?ie=UTF8&amp;qid=1431746869&amp;sr=8-12&amp;keywords=smartphones#customerReviews">148</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_12?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_12" data-asin="B00R7FPSDU" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-620G-Santroni-White/dp/B00R7FPSDU/ref=sr_1_13?ie=UTF8&amp;qid=1431746869&amp;sr=8-13&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41KzTVazeRL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="HTC Desire 620G (Dual SIM, Santroni White)" href="http://www.amazon.in/HTC-Desire-620G-Santroni-White/dp/B00R7FPSDU/ref=sr_1_13?ie=UTF8&amp;qid=1431746869&amp;sr=8-13&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">HTC Desire 620G (Dual SIM, Santroni White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">HTC</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-620G-Santroni-White/dp/B00R7FPSDU/ref=sr_1_13?ie=UTF8&amp;qid=1431746869&amp;sr=8-13&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>25,500.00</span></a><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-price">Only 1 left in stock - order soon.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00R7FPSDU/ref=sr_1_13_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-13&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>3 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>17,900.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00R7FPSDU">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00R7FPSDU&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4.1 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-620G-Santroni-White/dp/B00R7FPSDU/ref=sr_1_13?ie=UTF8&amp;qid=1431746869&amp;sr=8-13&amp;keywords=smartphones#customerReviews">218</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_13?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_13" data-asin="B00P2HZ81M" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Doodle-A102-Blue/dp/B00P2HZ81M/ref=sr_1_14?ie=UTF8&amp;qid=1431746869&amp;sr=8-14&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41-w5g%2BaPML._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Canvas Doodle 3 A102 (Blue, 8GB)" href="http://www.amazon.in/Micromax-Canvas-Doodle-A102-Blue/dp/B00P2HZ81M/ref=sr_1_14?ie=UTF8&amp;qid=1431746869&amp;sr=8-14&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Canvas Doodle 3 A102 (Blue, 8GB)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Doodle-A102-Blue/dp/B00P2HZ81M/ref=sr_1_14?ie=UTF8&amp;qid=1431746869&amp;sr=8-14&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>7,199.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>9,990.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>2,791.00
        (28%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-price">Only 1 left in stock - order soon.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00P2HZ81M/ref=sr_1_14_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-14&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>17 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>6,730.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00P2HZ81M">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00P2HZ81M&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Canvas-Doodle-A102-Blue/dp/B00P2HZ81M/ref=sr_1_14?ie=UTF8&amp;qid=1431746869&amp;sr=8-14&amp;keywords=smartphones#customerReviews">17</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_14?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_14" data-asin="B00M2VP1NQ" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-S850-White/dp/B00M2VP1NQ/ref=sr_1_15?ie=UTF8&amp;qid=1431746869&amp;sr=8-15&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41nHOfWKDfL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Lenovo S850 (White)" href="http://www.amazon.in/Lenovo-S850-White/dp/B00M2VP1NQ/ref=sr_1_15?ie=UTF8&amp;qid=1431746869&amp;sr=8-15&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Lenovo S850 (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Lenovo</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-S850-White/dp/B00M2VP1NQ/ref=sr_1_15?ie=UTF8&amp;qid=1431746869&amp;sr=8-15&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>9,749.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>17,999.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>8,250.00
        (46%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00M2VP1NQ/ref=sr_1_15_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-15&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>18 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>9,749.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00M2VP1NQ">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00M2VP1NQ&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.9 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Lenovo-S850-White/dp/B00M2VP1NQ/ref=sr_1_15?ie=UTF8&amp;qid=1431746869&amp;sr=8-15&amp;keywords=smartphones#customerReviews">366</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_15?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_15" data-asin="B00I0SL526" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A71-White/dp/B00I0SL526/ref=sr_1_16?ie=UTF8&amp;qid=1431746869&amp;sr=8-16&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/51M2errB6LL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, false);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Micromax Bolt A71 (White)" href="http://www.amazon.in/Micromax-Bolt-A71-White/dp/B00I0SL526/ref=sr_1_16?ie=UTF8&amp;qid=1431746869&amp;sr=8-16&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Micromax Bolt A71 (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Micromax</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A71-White/dp/B00I0SL526/ref=sr_1_16?ie=UTF8&amp;qid=1431746869&amp;sr=8-16&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>4,948.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>7,499.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>2,551.00
        (34%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00I0SL526/ref=sr_1_16_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-16&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>4 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>4,599.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00I0SL526">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00I0SL526&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-2-5"><span class="a-icon-alt">2.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Micromax-Bolt-A71-White/dp/B00I0SL526/ref=sr_1_16?ie=UTF8&amp;qid=1431746869&amp;sr=8-16&amp;keywords=smartphones#customerReviews">18</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_16?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li></ul></div><script type="text/javascript">
    P.now('A', 's-result-list').execute(function(A, sResultList) {
        var atfResults = document.getElementById("atfResults").childNodes[0],
            batchDiv = document.getElementById("btfResults").childNodes[0];
        if (A && sResultList && atfResults && batchDiv) {
            var children = A.$(btfResults).children();
            sResultList.appendItems(atfResults, A.$(batchDiv).children());
        }
        else if (atfResults && batchDiv) {
            var fragment = document.createDocumentFragment(),
                length = batchDiv.childNodes.length;

            for (var i = 0; i < length; i++){
                fragment.appendChild(batchDiv.childNodes[0]);
            }

            atfResults.appendChild(fragment);
        }
    });
    </script>
<div id="search-js-btr">
      <script type="text/javascript">



        amzn.sx.utils.jsDepMgr.when("jQuery ready", 'searchJsBtr', function($) {

          $("td.tpType").parent("tr").hover(
            function() { $(this).addClass("toeRowHover"); },
            function() { $(this).removeClass("toeRowHover"); });


          amzn.sx.utils.jsDepMgr.when("ImageRotation", 'setupImageRotation-atf-next', function (imageRotation) {
            imageRotation.setupImageRotation("atf");
            imageRotation.setupImageRotation("btf");
          });


        });

        amzn.sx.utils.jsDepMgr.when('search-js-general', 'processPromotionsPopover', function() {

          amzn.sx.utils.jsDepMgr.when('popover', 'promotionsPopover', function() {
            processPromotionsPopover();


          });


          SPUtils.triggerEvent("spResultsEnd");

          registerAivHandler("btf");


          if (typeof processBundlesFlyouts == 'function') {
              processBundlesFlyouts('btf');
          }


        });

      </script>
      </div>
  <div id="raw-search-js-btr" class="searchUndoAUIHacks">
















<div id="search-js-btr-external">
</div>


</div><div id="raw-search-desktop-advertising-tower-1" class="searchUndoAUIHacks">






      <div id="click_withinLazyLoad_tower" class="searchBreakAUI">
  </div>


  <script type="text/JavaScript">


(function() {
  P.when("A").execute(function (A) {
    var jQuery = A.$;
    var widgetName  = "click_within_tower";
    var keywords =  "smartphones";
    var searchAlias = "aps";
    var browseLadder = [];
      browseLadder.push("976419031");
    var childBrowseNode = "1805560031";
    var deviceType = "desktop";
    var pageType = "Search";
    var subPageType = "portal-batch-slow-btf";
    var profile = null;
    var extensions = undefined;
    var placement = "tower";
    var useAui = "1";
    var browseName = "";
    var hasRefinements = 0;
    var isSorted = 0;
    var specialtyRestriction = "";
    var hiddenKeywords ="";
    var vehicle = "";

    var widget = jQuery('#click_withinLazyLoad_tower');
    var stateKey = 'sponsoredProductsState';
    var layout = "list";
    var columns = 2;
    var pageNumber = 1;

    var existingState = A.state(stateKey);

    var seenAsins;

    var isNewLadder = function(a1, a2) {
      if (a1.length === 0 || a2.length === 0) {
        return true;
      }

      if (a1[0] !== a2[0]) {
        return true;
      }

      if (searchAlias !== "aps") {
        if (a1[a1.length - 1] !== a2[a2.length - 1]) {
          return true;
        }
      }

      return false;
    }

    if (typeof existingState !== "undefined") {
      if (existingState.keywords !== keywords) {
        seenAsins = [];
        existingState.keywords = keywords;
        existingState.browseLadder = browseLadder;
        existingState.seenAsins = [];
        A.state.replace(stateKey, existingState);
      } else if (isNewLadder(existingState.browseLadder, browseLadder)) {
        seenAsins = [];
        existingState.browseLadder = browseLadder;
        existingState.seenAsins = [];
        A.state.replace(stateKey, existingState);
      } else {
        seenAsins = existingState.seenAsins;
      }
    } else {
      var spData = {
        'keywords':keywords,
        'browseLadder':browseLadder,
        'seenAsins':[]
      }

      A.state(stateKey, spData);
    }

    var lazyLoadURL = '/gp/sponsored-products/lazyLoad/handler/click-within-handler.html';
    jQuery.ajax({

      url: lazyLoadURL + "?searchTerms="+keywords+
                         "&searchAlias="+encodeURIComponent(searchAlias)+
                         "&widgetName="+encodeURIComponent(widgetName)+
                         "&pageType=" + encodeURIComponent(pageType) +
                         "&subPageType=" + encodeURIComponent(subPageType) +
                         "&browseLadder="+encodeURIComponent(browseLadder)+
                         "&childBrowseNodes="+ encodeURIComponent(childBrowseNode) +
                         "&placement=" + encodeURIComponent(placement) +
                         "&seenasins="+encodeURIComponent(seenAsins)+
                         "&useAui=" + encodeURIComponent(useAui) +
                         "&browseName=" + encodeURIComponent(browseName) +
                         "&deviceType=" + encodeURIComponent(deviceType) +
                         "&profile=" + encodeURIComponent(profile) +
                         "&extensions=" + encodeURIComponent(extensions) +
                         "&hasRefinements=" + encodeURIComponent(hasRefinements) +
                         "&isSorted=" + encodeURIComponent(isSorted) +
                         "&specialtyRestriction=" + specialtyRestriction +
                         "&hiddenKeywords=" + hiddenKeywords +
                         "&vehicle=" + vehicle +
                         "&layout=" + encodeURIComponent(layout) +
                         "&columns=" + encodeURIComponent(columns) +
                         "&pageNumber=" + encodeURIComponent(pageNumber),

      type: "GET",
      cache : false,
      success : function(html) {
        widget.html(html);
      },
      error : function(html) {
        widget.html("<div></div>");
      }
    });
  });
})();

  </script>




















</div><div class="img_header hdr noborder" id="bottomBar">
    <div id="pagn" class="pagnHy" >
            <span class="pagnLA1"> <span class="srSprite firstPageLeftArrow"></span>
                    <span id="pagnPrevString">Previous Page</span></span>
                <span class="pagnCur">1</span>
                            <span class="pagnLink"><a href="/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Asmartphones&amp;page=2&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869" >2</a></span>
                            <span class="pagnLink"><a href="/s/ref=sr_pg_3?rh=i%3Aaps%2Ck%3Asmartphones&amp;page=3&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869" >3</a></span>
                            <span class="pagnMore">...</span>
                            <span class="pagnDisabled">20</span>
                            <span class="pagnRA"> <a title="AurDikhao"
                       id="pagnNextLink"
                       class="pagnNext"
                       href="/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Asmartphones&amp;page=2&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                        <span id="pagnNextString">AurDikhao</span>
                        <span class="srSprite pagnNextArrow"></span>
                     </a></span>
            <br clear="all" />
        </div>
    </div>

<div id="raw-seo-popular-around-the-web" class="searchUndoAUIHacks">
</div></div>

                            <div id="js-boot-btf">
                                <script>P.register('af');</script><script>P.register('cf');</script></div>

                            <div id="centerBelowExtra">
                                <div id="centerBelowExtra1"></div>
                                <div id="centerBelowExtraSponsoredLinks"></div>
                                <div id="centerBelowExtraHowsMySearch"><div id="hows-my-search" class="a-box a-spacing-large a-spacing-top-small"><div class="a-box-inner"><div class="a-row a-spacing-small"><div id="sx-hms-heading" class="a-section a-spacing-none" role="region"><h4 class="a-color-secondary">Search Feedback</h4><span>Did you find what you were looking for?</span></div><ul class="a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-none a-spacing-top-micro" role="radiogroup" data-action="a-button-group" data-a-button-group="{&quot;name&quot;:&quot;toggleSearchFeedbackType&quot;}"><li><span class="a-list-item"><span class="a-button a-button-toggle"><span class="a-button-inner"><input name="sx-feedback-yes" title="Yes" class="a-button-input" type="submit"><span class="a-button-text" aria-hidden="true">Yes</span></span></span></span></li><li><span class="a-list-item"><span class="a-button a-button-toggle"><span class="a-button-inner"><input name="sx-feedback-no" title="No" class="a-button-input" type="submit"><span class="a-button-text" aria-hidden="true">No</span></span></span></span></li></ul><form id="sx-hms-response-form" method="post" action="/gp/search/hmsfeedback/ref=sr_hms_f" class="a-spacing-none"><div id="sx-hms-category-list" style="display: none">
                    <p class="a-spacing-top-small"><label>Choose a category that best describes the issue that you are having with the search:</label><span class="a-dropdown-container"><select name="category" autocomplete="off" class="a-native-dropdown"><option class="a-prompt" value="">&hellip;</option><option value="CUSTOMER_SVC">I need to talk to customer service.</option><option value="FIND_ITEM">I still haven&#039;t found what I&#039;m looking for.</option><option value="NARROW_OR_SORT">How do I filter or sort my search ?</option><option value="OTHER">Something broken.</option><option value="INCORRECT_DESC">A picture or description looks wrong.</option><option value="FEATURE_REQUEST">Could you add a feature ?</option><option value="ITEM_REQUEST">Could you start carrying a product not listed here ?</option></select><span tabIndex="-1" id="sx-hms-categoy-dropdown" class="a-button a-button-dropdown"><span class="a-button-inner"><span class="a-button-text a-declarative" data-action="a-dropdown-button" aria-haspopup="true" role="button" tabIndex="0"><span class="a-dropdown-prompt">&hellip;</span></span><i class="a-icon a-icon-dropdown"></i></span></span></span></p></div>

                <div id="sx-hms-response" style="display: none">
                    <input type="hidden" name="qid" value="1431746869">
                    <input type="hidden" name="keywords" value="smartphones">
                    <input type="hidden" name="store" value="gateway">
                    <input type="hidden" name="url" value="http://www.amazon.in/s?url=search-alias%3Daps&amp;field-keywords=smartphones&amp;sprefix=smartphones%2Caps">
                    <input type="hidden" name="vote" value="" id="sx-hms-vote" />

                    <p class="a-spacing-none a-spacing-top-small"><label>Leave us some comments about your search; your comments can help make our site better for everyone.</label></p><div class="a-input-text-wrapper a-spacing-mini"><textarea placeholder="Please note that we are unable to respond directly to feedback submitted via this form." id="sx-hms-response-text" rows="5" name="response"></textarea></div><span class="a-button a-button-primary"><span class="a-button-inner"><input name="submit" title="Submit" class="a-button-input" type="submit" value="submit"><span class="a-button-text" aria-hidden="true">Submit</span></span></span></div>
            </form><div id="sx-hms-customer-support" style="display: none">
                <div class="a-box a-alert a-alert-info a-spacing-top-small"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">Get Express customer service or contact us by e-mail or phone.<span class="a-letter-space"></span><span class="a-button a-button-primary"><span class="a-button-inner"><a href="/gp/help/contact-us/general-questions.html/ref=sr_hms_cs?browse_node_id=200533820&amp;ie=UTF8&amp;qid=1431746869" class="a-button-text" role="button">contact us</a></span></span></div></div></div></div>

            <div id="sx-hms-response-sent" style="display: none;">
                <div class="a-box a-alert a-alert-success"><div class="a-box-inner a-alert-container"><i class="a-icon a-icon-alert"></i><div class="a-alert-content">Thank you for your feedback.</div></div></div></div>
        </div><div class="a-row"><span>If you need help or have a question for Customer Service, please <a class="a-link-normal a-text-normal" href="/gp/help/customer/display.html/ref=sr_hms_help?nodeId=200533820&amp;ie=UTF8&amp;qid=1431746869">visit the Help Section</a>.</span></div></div></div></div>
                                <div id="centerBelowExtra2"></div>
                                <div id="centerBelowExtra3"><div id="poweredBy">
<span class="text" >Search powered by</span>
<a href="http://a9.com/?src=amz_spb_sas"><img src="http://g-ecx.images-amazon.com/images/G/31/search-browse/powered-by-a9._CB138348993_.gif" alt="A9" width="24" height="24" border="0"/></a>
</div>
</div>
                            </div>

                </div>
                    </div>

                    <div id="leftNav">
                        <div id="leftNavPrefix">
                            </div>
                        <div id="leftNavContainer">
                            <div id="refinements" data-baserh="i%3Aaps%2Ck%3Asmartphones" data-browseladder="i%3Aaps">
<div class="shoppingEngineSectionHeaders">
            Show results for</div>
        <div class="categoryRefinementsSection">
        <ul class="forExpando" data-typeid="n">
    <li>
                    <a href="/s/ref=sr_nr_n_0?fst=as%3Aoff&amp;rh=n%3A976419031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
                             <span class="boldRefinementLink">Electronics</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          <ul class="refinementNodeChildren" data-typeid="n">
                    <li>
          <a href="/s/ref=sr_nr_n_1?fst=as%3Aoff&amp;rh=n%3A1805560031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Smartphones</span></a>
          </li>
          </ul>
                                <ul id="seeMoreRefinementValuesClosed1" class="refinementNodeHiddenChildren">
                                    <li>
                                    <span style="white-space:nowrap;">
                                        <a href="#"
                                           class="s-hack-show-hide-el"
                                           data-el-to-hide="#seeMoreRefinementValuesClosed1"
                                           data-el-to-show="#seeMoreRefinementValuesOpen1">
                                            <span class="expander">+</span>
                                            <span class="refinementLink seeMore">
                                                See more</span>
                                        </a>
                                    </span>
                                    </li>
                                </ul>
                                <ul style="display:none;" id="seeMoreRefinementValuesOpen1" class="refinementNodeHiddenChildren">
                            <li>
          <a href="/s/ref=sr_nr_n_2?fst=as%3Aoff&amp;rh=n%3A1389405031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Batteries</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_3?fst=as%3Aoff&amp;rh=n%3A1389409031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Cases &amp; Covers</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_4?fst=as%3Aoff&amp;rh=n%3A1389432031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Smartphones &amp; Basic Mobiles</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_5?fst=as%3Aoff&amp;rh=n%3A1389422031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Mounts &amp; Stands</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_6?fst=as%3Aoff&amp;rh=n%3A1389417031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Data Cables</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_7?fst=as%3Aoff&amp;rh=n%3A1389407031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Car Cradles</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_8?fst=as%3Aoff&amp;rh=n%3A1388921031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Headphones</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_9?fst=as%3Aoff&amp;rh=n%3A1389403031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Accessory Kits</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_10?fst=as%3Aoff&amp;rh=n%3A1389411031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Mobile Phone Car Chargers</span></a>
          </li>
          <li id="fewDep">
                        <span style="white-space:nowrap;">
                            <a href="#"
                               class="s-hack-show-hide-el"
                               data-el-to-hide="#seeMoreRefinementValuesOpen1"
                               data-el-to-show="#seeMoreRefinementValuesClosed1">

                               <span class="expander">-</span>
                               <span class="refinementLink seeMore">
                                    See Less</span>
                            </a>
                        </span>
                        </li>
                    </ul>
              </li>
            </ul>
            <ul style="display:none;" id="seeAllDepartmentClosed1" data-typeid="n">
                <li style="margin-left: -20px;">
                            <span style="white-space:nowrap;">
                    <a href="#"
                       class="s-hack-show-hide-el"
                       data-el-to-show="#seeAllDepartmentOpen1"
                       data-el-to-hide="#seeAllDepartmentClosed1">
                        <span class="expander">+</span>
                            <span class="refinementLink seeMore">
                                    See All 19 Departments</span>
                    </a>
                </span>
                </li>
            </ul>
            <ul style="display:block;" id="seeAllDepartmentOpen1" data-typeid="n" class="seeAllSmartRefDepartmentOpen">
                <li>
                    <a href="/s/ref=sr_nr_n_11?fst=as%3Aoff&amp;rh=n%3A976392031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
                             <span class="boldRefinementLink">Computers &amp; Accessories</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          <ul class="refinementNodeChildren" data-typeid="n">
                    <li>
          <a href="/s/ref=sr_nr_n_12?fst=as%3Aoff&amp;rh=n%3A1375422031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Pens for Graphic Tablets</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_13?fst=as%3Aoff&amp;rh=n%3A1375287031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">USB Cables</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_14?fst=as%3Aoff&amp;rh=n%3A1375331031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Chargers, Adapters &amp; Cables for Touch Screen Tablets</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_15?fst=as%3Aoff&amp;rh=n%3A1375334031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Touch Screen Tablet Stands</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_16?fst=as%3Aoff&amp;rh=n%3A1375411031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Pen Drives</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_17?fst=as%3Aoff&amp;rh=n%3A1375419031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Keyboards</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_18?fst=as%3Aoff&amp;rh=n%3A2559723031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">DisplayPort Cables</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_19?fst=as%3Aoff&amp;rh=n%3A1375310031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Portable Computer Chargers &amp; Power Supplies</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_20?fst=as%3Aoff&amp;rh=n%3A1375342031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">USB Hubs</span></a>
          </li>
          </ul>
              </li>
            <li>
                    <a href="/s/ref=sr_nr_n_21?fst=as%3Aoff&amp;rh=n%3A1350380031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
                             <span class="boldRefinementLink">Toys &amp; Games</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          <ul class="refinementNodeChildren" data-typeid="n">
                    <li>
          <a href="/s/ref=sr_nr_n_22?fst=as%3Aoff&amp;rh=n%3A1378336031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Sport Games</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_23?fst=as%3Aoff&amp;rh=n%3A1378381031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Model Rocket &amp; Spaceship Kits</span></a>
          </li>
          </ul>
              </li>
            <li>
                    <a href="/s/ref=sr_nr_n_24?fst=as%3Aoff&amp;rh=n%3A976389031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
                             <span class="boldRefinementLink">Books</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          <ul class="refinementNodeChildren" data-typeid="n">
                    <li>
          <a href="/s/ref=sr_nr_n_25?fst=as%3Aoff&amp;rh=n%3A1318112031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Computer Hardware &amp; Handheld Devices</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_26?fst=as%3Aoff&amp;rh=n%3A1318185031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Reference</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_27?fst=as%3Aoff&amp;rh=n%3A1318071031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Industries &amp; Business Sectors</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_28?fst=as%3Aoff&amp;rh=n%3A1318108031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Computer Science</span></a>
          </li>
          <li>
          <a href="/s/ref=sr_nr_n_29?fst=as%3Aoff&amp;rh=n%3A1318209031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Engineering &amp; Technology</span></a>
          </li>
          </ul>
              </li>
            <li>
                    <a href="/s/ref=sr_nr_n_30?fst=as%3Aoff&amp;rh=n%3A1350387031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
                             <span class="boldRefinementLink">Watches</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          <ul class="refinementNodeChildren" data-typeid="n">
                    <li>
          <a href="/s/ref=sr_nr_n_31?fst=as%3Aoff&amp;rh=n%3A1375495031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">
            <span class="childRefinementLink">Wristwatches</span></a>
          </li>
          </ul>
              </li>
            <li>
                    <a href="/s/ref=sr_nr_i_32?rh=k%3Asmartphones%2Ci%3Amisc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Everything Else</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_33?rh=k%3Asmartphones%2Ci%3Adigital-text&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Kindle Store</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_34?rh=k%3Asmartphones%2Ci%3Aautomotive&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Car &amp; Motorbike</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_35?rh=k%3Asmartphones%2Ci%3Asporting&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Sports, Fitness &amp; Outdoors</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_36?rh=k%3Asmartphones%2Ci%3Akitchen&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Home &amp; Kitchen</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_37?rh=k%3Asmartphones%2Ci%3Ababy&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Baby</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_38?rh=k%3Asmartphones%2Ci%3Ahpc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Health &amp; Personal Care</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_39?rh=k%3Asmartphones%2Ci%3Ami&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Musical Instruments</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_40?rh=k%3Asmartphones%2Ci%3Aoffice-products&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Office Products</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_41?rh=k%3Asmartphones%2Ci%3Aluggage&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Luggage &amp; Bags</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_42?rh=k%3Asmartphones%2Ci%3Avideogames&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Video Games</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_43?rh=k%3Asmartphones%2Ci%3Asoftware&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Software</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_44?rh=k%3Asmartphones%2Ci%3Aapparel&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Clothing &amp; Accessories</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li>
                    <a href="/s/ref=sr_nr_i_45?rh=k%3Asmartphones%2Ci%3Ashoes&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">
                             <span class="boldRefinementLink">Shoes &amp; Handbags</span>
                             <span class="srSprite rightArrow"></span>
                           </a>
                          </li>
            <li id="fewDep" style="margin-top: 6px;">
            <span style="white-space:nowrap;">
            <a href="#"
               class="s-hack-show-hide-el"
               data-el-to-show="#seeAllDepartmentClosed1"
               data-el-to-hide="#seeAllDepartmentOpen1">
               <span class="expander">-</span>
                    <span class="refinementLink seeMore">
                            See Fewer Departments</span>
            </a>
        </span>
        </li>
    </ul>

<script type="text/javascript">


    amzn.sx.utils.jsDepMgr.when('jQuery', 'deptRefinementCollapseExpand', function($) {

        function init(){
            setupView();
            addListeners();
        }

        function setupView(){
            $('#seeAllDepartmentClosed1').show();
            $('#fewDep').show();
            $('#seeAllDepartmentOpen1').hide();
        }

        function addListeners(){
            $showHideLinks.click( handleToggleLinkClick );
            $smartAPSSortUpdate.click( handleSmartAPSSortUpdate);
        }

        function handleToggleLinkClick( e ){
            var $el = $( e.currentTarget ),
                elToShow = $el.attr( "data-el-to-show"),
                elToHide = $el.attr( "data-el-to-hide");
            toggleElements( $( elToShow ),  $( elToHide ) );
            e.preventDefault();
            return false;
        }

        function handleSmartAPSSortUpdate(e){
            var dynamicID = $(e.currentTarget).attr("data-dynamic-id");
            smartAPSSortUpdate( dynamicID );
            e.preventDefault();
            return false;
        }

        function toggleElements( $toShow, $toHide ){
            $toHide.hide();
            $toShow.show();
        }


        var $showHideLinks = $(".s-hack-show-hide-el"),
            $smartAPSSortUpdate = $(".s-hack-smart-aps-sort-update");


        init();

    });

 </script>
</div>
         <div class="shoppingEngineSectionHeaders">Refine by</div>
        <h2>Fulfilled By<span class="shippingWhatsThis">

(<a href="/gp/help/customer/display.html/ref=sr_nr_p_76_whatsthis?nodeId=200953360&amp;pop-up=1&amp;ie=UTF8&amp;qid=1431746869" target="WhatsThisHelp" onclick="return amz_js_PopWin(this.href,'WhatsThisHelp','width=800,height=600,resizable=1,scrollbars=1,toolbar=1,status=1');">What's this?</a>)
</span>
    </h2>
<ul id="ref_1318480031" >
     <li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_76_1?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_76%3A1318482031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1318480031" class=" ">
      <img style="margin-right:4px; margin-top:2px;" height="11" width="11" border="0" align="bottom"
                    alt="Fulfilled by Amazon" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png">
        <span class="refinementLink "

    >Amazon</span>
    <img style="margin-right: 4px;margin-left:2px;" height="18" width="66" border="0" align="top"
                         alt="Fulfilled by Amazon" src="http://g-ecx.images-amazon.com/images/G/31/marketing/fba/fba-badge_18px._CB384100965_.png" />
                </a>
      </li>
</ul>

<h2>Cash On Delivery<span class="shippingWhatsThis">

(<a href="/gp/help/customer/display.html/ref=sr_nr_p_n_is_cod_eligible_whatsthis?nodeId=200904360&amp;pop-up=1&amp;ie=UTF8&amp;qid=1431746869" target="WhatsThisHelp" onclick="return amz_js_PopWin(this.href,'WhatsThisHelp','width=800,height=600,resizable=1,scrollbars=1,toolbar=1,status=1');">What's this?</a>)
</span>
    </h2>
<ul id="ref_4931670031" >
     <li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_is_cod_eligible_0?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_n_is_cod_eligible%3A4931671031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=4931670031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Eligible for Cash On Delivery" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Eligible for Cash On Delivery</span>
    </a>
      </li>
</ul>

<h2>Mobile Phone Operating System</h2>
<ul id="ref_1485076031" data-typeid="n" >
     <li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_operating_system_0?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_operating_system_browse-bin%3A1485077031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1485076031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Android" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Android</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_operating_system_1?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_operating_system_browse-bin%3A1485084031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1485076031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Windows Phone" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Windows Phone</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_operating_system_2?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_operating_system_browse-bin%3A1485080031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1485076031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="iOS" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >iOS</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_operating_system_3?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_operating_system_browse-bin%3A1485079031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1485076031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Blackberry" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Blackberry</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_operating_system_4?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_operating_system_browse-bin%3A1485082031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1485076031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Symbian" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Symbian</span>
    </a>
      </li>
</ul>

<h2>Mobile Phone Features</h2>
<ul class="forExpando" data-typeid="n">
    <li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_0?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1897963031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Dual SIM" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Dual SIM</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_1?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484944031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="E-Mail" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >E-Mail</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_2?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484949031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Touchscreen" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Touchscreen</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_3?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484942031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Primary Camera" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Primary Camera</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_4?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1897966031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Music Player" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Music Player</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_5?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484945031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="GPS" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >GPS</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_6?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1897958031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Wifi Hotspot" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Wifi Hotspot</span>
    </a>
      </li>
</ul>
            <ul style="display:none;" id="seeAllDepartmentClosed5" data-typeid="n">
                <li style="margin-left: 6px;">
                            <span style="white-space:nowrap;">
                    <a href="#"
                       class="s-hack-show-hide-el"
                       data-el-to-show="#seeAllDepartmentOpen5"
                       data-el-to-hide="#seeAllDepartmentClosed5">
                        <span class="expander">+</span>
                            <span class="refinementLink seeMore subCategories">
                                    See more</span>
                    </a>
                </span>
                </li>
            </ul>
            <ul style="display:block;" id="seeAllDepartmentOpen5" data-typeid="n">
                <li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_7?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484950031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="USB" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >USB</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_8?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484948031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Radio" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Radio</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_9?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484947031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="MP3" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >MP3</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_10?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484951031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="WAP" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >WAP</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_11?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484952031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Wifi" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Wifi</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_12?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1484946031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Internet" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Internet</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_13?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A6612094031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Secondary Camera" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Secondary Camera</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: 8px">
    <a href="/s/ref=sr_nr_p_n_feature_three_br_14?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_three_browse-bin%3A1897961031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1484941031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Video Playback" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Video Playback</span>
    </a>
      </li>
<li id="fewDep" style="margin-top: 6px;">
            <span style="white-space:nowrap;">
            <a href="#"
               class="s-hack-show-hide-el"
               data-el-to-show="#seeAllDepartmentClosed5"
               data-el-to-hide="#seeAllDepartmentOpen5">
               <span class="expander">-</span>
                    <span class="refinementLink seeMore subCategories">
                            See Less</span>
            </a>
        </span>
        </li>
    </ul>

<script type="text/javascript">


    amzn.sx.utils.jsDepMgr.when('jQuery', 'deptRefinementCollapseExpand', function($) {

        function init(){
            setupView();
            addListeners();
        }

        function setupView(){
            $('#seeAllDepartmentClosed5').show();
            $('#fewDep').show();
            $('#seeAllDepartmentOpen5').hide();
        }

        function addListeners(){
            $showHideLinks.click( handleToggleLinkClick );
            $smartAPSSortUpdate.click( handleSmartAPSSortUpdate);
        }

        function handleToggleLinkClick( e ){
            var $el = $( e.currentTarget ),
                elToShow = $el.attr( "data-el-to-show"),
                elToHide = $el.attr( "data-el-to-hide");
            toggleElements( $( elToShow ),  $( elToHide ) );
            e.preventDefault();
            return false;
        }

        function handleSmartAPSSortUpdate(e){
            var dynamicID = $(e.currentTarget).attr("data-dynamic-id");
            smartAPSSortUpdate( dynamicID );
            e.preventDefault();
            return false;
        }

        function toggleElements( $toShow, $toHide ){
            $toHide.hide();
            $toShow.show();
        }


        var $showHideLinks = $(".s-hack-show-hide-el"),
            $smartAPSSortUpdate = $(".s-hack-smart-aps-sort-update");


        init();

    });

 </script>
<h2>Mobile Phone Camera Resolution</h2>
<ul id="ref_1898694031" data-typeid="n" >
     <li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_feature_two_brow_0?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_two_browse-bin%3A1898703031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1898694031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Up to 2.9 MP" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Up to 2.9 MP</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_feature_two_brow_1?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_two_browse-bin%3A1898704031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1898694031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="3 - 4.9 MP" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >3 - 4.9 MP</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_feature_two_brow_2?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_two_browse-bin%3A1898705031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1898694031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="5 - 7.9 MP" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >5 - 7.9 MP</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_feature_two_brow_3?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_two_browse-bin%3A1898706031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1898694031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="8 - 9.9 MP" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >8 - 9.9 MP</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_n_feature_two_brow_4?fst=as%3Aoff&amp;rh=n%3A1389401031%2Ck%3Asmartphones%2Cp_n_feature_two_browse-bin%3A1898707031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1898694031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="10 MP &amp; more" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >10 MP &amp; more</span>
    </a>
      </li>
</ul>

<h2>Brand</h2>
<ul id="ref_3837712031" >
     <li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_0?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ALenovo&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Lenovo" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Lenovo</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_1?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AMicromax&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Micromax" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Micromax</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_2?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AIntex&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Intex" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Intex</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_3?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ASamsung&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Samsung" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Samsung</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_4?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AXOLO&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="XOLO" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >XOLO</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_5?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ASpice&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Spice" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Spice</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_6?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AMi&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Mi" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Mi</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_7?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ASmartphone&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Smartphone" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Smartphone</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_8?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AKarbonn&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Karbonn" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Karbonn</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_9?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ASony&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Sony" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Sony</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_10?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AHTC&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="HTC" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >HTC</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_11?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ANokia&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Nokia" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Nokia</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_12?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3ALava&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Lava" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Lava</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_13?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3AApple&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Apple" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Apple</span>
    </a>
      </li>
<li class="refinementImage" style="margin-left: -10px">
    <a href="/s/ref=sr_nr_p_89_14?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_89%3APanasonic&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3837712031" class=" ">
      <img height="11" width="11" border="0" align="bottom"
                    alt="Panasonic" src="http://g-ecx.images-amazon.com/images/G/31/shopping_engine/nav2/buttons/checkbox_unselected_enabled._CB341434301_.png" />
             &#8202;<span class="refinementLink"

    >Panasonic</span>
    </a>
      </li>
</ul>

<h2>Avg. Customer Review</h2>
<ul id="ref_1318475031" style="border:none;" >
     <li class="refinementImage" style="margin-left: -2px">
    <a href="/s/ref=sr_nr_p_72_0?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_72%3A1318476031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1318475031">
                <i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">4 Stars &amp; Up</span></i><span class="refinementLink">&amp; Up</span>
                </a>
        </li><li class="refinementImage" style="margin-left: -2px">
    <a href="/s/ref=sr_nr_p_72_1?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_72%3A1318477031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1318475031">
                <i class="a-icon a-icon-star a-star-3"><span class="a-icon-alt">3 Stars &amp; Up</span></i><span class="refinementLink">&amp; Up</span>
                </a>
        </li><li class="refinementImage" style="margin-left: -2px">
    <a href="/s/ref=sr_nr_p_72_2?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_72%3A1318478031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1318475031">
                <i class="a-icon a-icon-star a-star-2"><span class="a-icon-alt">2 Stars &amp; Up</span></i><span class="refinementLink">&amp; Up</span>
                </a>
        </li><li class="refinementImage" style="margin-left: -2px">
    <a href="/s/ref=sr_nr_p_72_3?fst=as%3Aoff&amp;rh=i%3Aaps%2Ck%3Asmartphones%2Cp_72%3A1318479031&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=1318475031">
                <i class="a-icon a-icon-star a-star-1"><span class="a-icon-alt">1 Star &amp; Up</span></i><span class="refinementLink">&amp; Up</span>
                </a>
        </li></ul>

<hr class="s-wayfinding-rule" />
    </div></div>
                        <div id="leftNavPostfix">
                            <script type="text/javascript">
    amzn.sx.utils.jsDepMgr.when('search-js-general', "search-content-end", function() {

       SPUtils.triggerEvent("spSearchContentEnd");
    });
</script>
</div>
                        <div id="leftNavAdvertising">
                            </div>
                    </div>

                <div id="ajaxData">
                    <div id="results-atf-next" style="display: none;">
    <!--
<div id="atfResults" class="a-row s-result-list-parent-container"><ul id="s-results-list-atf" class="s-result-list s-col-1 s-col-ws-1 s-result-list-hgrid s-height-equalized s-list-view s-text-condensed"><li id="result_16" data-asin="B00OK2ZW5W" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/OnePlus-One-64GB-Sandstone-Black/dp/B00OK2ZW5W/ref=sr_1_17?ie=UTF8&amp;qid=1431746869&amp;sr=8-17&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41HSXF%2B4IEL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="OnePlus One (64GB, Sandstone Black)" href="http://www.amazon.in/OnePlus-One-64GB-Sandstone-Black/dp/B00OK2ZW5W/ref=sr_1_17?ie=UTF8&amp;qid=1431746869&amp;sr=8-17&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">OnePlus One (64GB, Sandstone Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">OnePlus</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/OnePlus-One-64GB-Sandstone-Black/dp/B00OK2ZW5W/ref=sr_1_17?ie=UTF8&amp;qid=1431746869&amp;sr=8-17&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>21,998.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>21,999.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>1.00</span></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00OK2ZW5W">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00OK2ZW5W&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4-5"><span class="a-icon-alt">4.4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/OnePlus-One-64GB-Sandstone-Black/dp/B00OK2ZW5W/ref=sr_1_17?ie=UTF8&amp;qid=1431746869&amp;sr=8-17&amp;keywords=smartphones#customerReviews">13,473</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_17?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_17" data-asin="B00VEB0N6A" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-Note-4G-White/dp/B00VEB0N6A/ref=sr_1_18?ie=UTF8&amp;qid=1431746869&amp;sr=8-18&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41mENUJoXxL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Redmi Note 4G (White)" href="http://www.amazon.in/Mi-Redmi-Note-4G-White/dp/B00VEB0N6A/ref=sr_1_18?ie=UTF8&amp;qid=1431746869&amp;sr=8-18&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Redmi Note 4G (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Mi</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-Note-4G-White/dp/B00VEB0N6A/ref=sr_1_18?ie=UTF8&amp;qid=1431746869&amp;sr=8-18&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>9,999.00</span></a><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00VEB0N6A">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00VEB0N6A&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Mi-Redmi-Note-4G-White/dp/B00VEB0N6A/ref=sr_1_18?ie=UTF8&amp;qid=1431746869&amp;sr=8-18&amp;keywords=smartphones#customerReviews">173</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_18?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_18" data-asin="B00LSPHFCC" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Samsung-Galaxy-Core-2-White/dp/B00LSPHFCC/ref=sr_1_19?ie=UTF8&amp;qid=1431746869&amp;sr=8-19&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41nLnL5VIeL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Samsung Galaxy Core 2 (White)" href="http://www.amazon.in/Samsung-Galaxy-Core-2-White/dp/B00LSPHFCC/ref=sr_1_19?ie=UTF8&amp;qid=1431746869&amp;sr=8-19&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Samsung Galaxy Core 2 (White)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Samsung</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Samsung-Galaxy-Core-2-White/dp/B00LSPHFCC/ref=sr_1_19?ie=UTF8&amp;qid=1431746869&amp;sr=8-19&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>7,350.00</span></a><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00LSPHFCC/ref=sr_1_19_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-19&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>33 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>7,170.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00LSPHFCC">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00LSPHFCC&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Samsung-Galaxy-Core-2-White/dp/B00LSPHFCC/ref=sr_1_19?ie=UTF8&amp;qid=1431746869&amp;sr=8-19&amp;keywords=smartphones#customerReviews">154</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_19?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_19" data-asin="B00STZZ88W" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-816G-Octa-core-Dual/dp/B00STZZ88W/ref=sr_1_20?ie=UTF8&amp;qid=1431746869&amp;sr=8-20&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41qXLrdD4QL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="HTC Desire 816G+ Octa-core (Dual SIM, 16GB, Blue)" href="http://www.amazon.in/HTC-Desire-816G-Octa-core-Dual/dp/B00STZZ88W/ref=sr_1_20?ie=UTF8&amp;qid=1431746869&amp;sr=8-20&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">HTC Desire 816G+ Octa-core (Dual SIM, 16GB, Blue)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">HTC</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-816G-Octa-core-Dual/dp/B00STZZ88W/ref=sr_1_20?ie=UTF8&amp;qid=1431746869&amp;sr=8-20&amp;keywords=smartphones"><span class="a-size-base a-color-price s-price a-text-bold"><span class="currencyINR">&nbsp;&nbsp;</span>16,017.00</span></a><span class="a-letter-space"></span><span class="a-size-small a-color-secondary a-text-strike"><span class="currencyINR">&nbsp;&nbsp;</span>21,990.00</span><span class="a-letter-space"></span><i class="a-icon-wrapper a-icon-small a-icon-fba-with-text"><i class="a-icon a-icon-fba"></i><span class="a-icon-text-fba">Fulfilled</span></i></div><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">You Save: </span><span class="a-size-small a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span>5,973.00
        (27%)
    </span></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><div class="a-row a-spacing-mini"></div><span class="a-size-small a-color-secondary">More Buying Choices</span></div><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00STZZ88W/ref=sr_1_20_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-20&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>17 offers<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>16,017.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00STZZ88W">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00STZZ88W&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-4"><span class="a-icon-alt">3.8 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/HTC-Desire-816G-Octa-core-Dual/dp/B00STZZ88W/ref=sr_1_20?ie=UTF8&amp;qid=1431746869&amp;sr=8-20&amp;keywords=smartphones#customerReviews">71</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary"><b>FREE Delivery</b> on orders over Rs.499.<br/>Cash on Delivery eligible.</span></div></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_20?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_20" data-asin="B00IKC6VQW" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/XOLO-A500-Club-Xolo-Black/dp/B00IKC6VQW/ref=sr_1_21?ie=UTF8&amp;qid=1431746869&amp;sr=8-21&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/41GYyTG-DIL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Xolo A500 Club (Black)" href="http://www.amazon.in/XOLO-A500-Club-Xolo-Black/dp/B00IKC6VQW/ref=sr_1_21?ie=UTF8&amp;qid=1431746869&amp;sr=8-21&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Xolo A500 Club (Black)</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">XOLO</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00IKC6VQW/ref=sr_1_21_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-21&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>1 offer<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>7,890.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00IKC6VQW">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00IKC6VQW&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-3-5"><span class="a-icon-alt">3.6 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/XOLO-A500-Club-Xolo-Black/dp/B00IKC6VQW/ref=sr_1_21?ie=UTF8&amp;qid=1431746869&amp;sr=8-21&amp;keywords=smartphones#customerReviews">147</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_21?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li><li id="result_21" data-asin="B00OBBUONW" class="s-result-item"><div class="s-item-container"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:160px"><div class="a-fixed-left-grid-col a-col-left" style="width:160px;margin-left:-160px;_margin-left:-80px;float:left;"><div class="a-row"><div class="a-column a-span12 a-text-center"><a class="a-link-normal a-text-normal" href="http://www.amazon.in/Cheers-C21-3-5-Inches-Smartphone/dp/B00OBBUONW/ref=sr_1_22?ie=UTF8&amp;qid=1431746869&amp;sr=8-22&amp;keywords=smartphones"><img alt="Product Details" src="http://ecx.images-amazon.com/images/I/414zUk308bL._AA160_.jpg" onload="viewCompleteImageLoaded(this, new Date().getTime(), 16, true);(function(ueAjaxT){if (typeof uet == 'function' && window.amzn && amzn.sx && amzn.sx.utils && amzn.sx.utils.jsDepMgr) {amzn.sx.utils.jsDepMgr.when('jQuery','ajax_ue_ajax_manageLoad', function(jQuery) { if (jQuery.searchUE) { ues('ctb', jQuery.searchUE.getScope(), '1');uet('af', jQuery.searchUE.getScope(), {}, ueAjaxT);jQuery.searchUE.manageLoad(); }});}})((new Date()).getTime()); if(window.amzn && amzn.sx && amzn.sx.utils && amzn.sx.utils.jsDepMgr) {amzn.sx.utils.jsDepMgr.when('search-js-general','atf_event_trigger', function() {SPUtils.triggerATFEvent(0);});}" class="s-access-image cfMarker" height="160" width="160"></a></div></div></div><div class="a-fixed-left-grid-col a-col-right" style="padding-left:2%;*width:97.6%;float:left;"><div class="a-row a-spacing-small"><a class="a-link-normal s-access-detail-page  a-text-normal" title="Cheers C21 3.5 Inches Smartphone" href="http://www.amazon.in/Cheers-C21-3-5-Inches-Smartphone/dp/B00OBBUONW/ref=sr_1_22?ie=UTF8&amp;qid=1431746869&amp;sr=8-22&amp;keywords=smartphones"><h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">Cheers C21 3.5 Inches Smartphone</h2></a><div class="a-row a-spacing-none"><span class="a-size-small a-color-secondary">by </span><span class="a-size-small a-color-secondary">Cheers</span></div></div><div class="a-row"><div class="a-column a-span7"><div class="a-row a-spacing-mini"><div class="a-row a-spacing-none"><a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/gp/offer-listing/B00OBBUONW/ref=sr_1_22_olp?ie=UTF8&amp;qid=1431746869&amp;sr=8-22&amp;keywords=smartphones&amp;condition=new"><span class="a-size-base a-color-price a-text-bold"></span><span class="a-letter-space"></span>1 offer<span class="a-letter-space"></span><span class="a-color-price">from <span class="currencyINR">&nbsp;&nbsp;</span>1,599.00</span><span class="a-letter-space"></span><span class="a-color-secondary a-text-strike"></span></a></div></div></div><div class="a-column a-span5 a-span-last"><div class="a-row a-spacing-mini"><span name="B00OBBUONW">
    <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;position&quot;:&quot;triggerBottom&quot;,&quot;max-width&quot;:&quot;700&quot;,&quot;closeButton&quot;:&quot;false&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B00OBBUONW&amp;contextId=search&amp;ref=acr_search__popover&quot;}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star a-star-2-5"><span class="a-icon-alt">2.4 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span></span>

<a class="a-size-small a-link-normal a-text-normal" href="http://www.amazon.in/Cheers-C21-3-5-Inches-Smartphone/dp/B00OBBUONW/ref=sr_1_22?ie=UTF8&amp;qid=1431746869&amp;sr=8-22&amp;keywords=smartphones#customerReviews">7</a></div><div class="a-row a-spacing-mini"><div class="a-row a-spacing-mini"><a class="a-size-small a-link-normal a-text-normal" href="/s/ref=sr_nr_seeall_22?rh=k%3Asmartphones%2Ci%3Aelectronics&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869"><span class="a-text-bold">Electronics:</span><span class="a-letter-space"></span>See all 6,303 items</a></div></div></div></div></div></div></div></div></li></ul></div>
    -->
    </div>
<script type="text/javascript">
    P.now('A', 's-result-list').execute(function(A, sResultList) {
        var atfResults = document.getElementById("atfResults").childNodes[0],
            batchDiv = document.getElementById("results-atf-next").childNodes[0];
        if (A && sResultList && atfResults && batchDiv) {
            var children = A.$(btfResults).children();
            sResultList.appendItems(atfResults, A.$(batchDiv).children());
        }
        else if (atfResults && batchDiv) {
            var fragment = document.createDocumentFragment(),
                length = batchDiv.childNodes.length;

            for (var i = 0; i < length; i++){
                fragment.appendChild(batchDiv.childNodes[0]);
            }

            atfResults.appendChild(fragment);
        }
    });
    </script>
<div id="result-count-only-next" style="display: none;">
    <!--
        <h2 class="resultCount" id="resultCount"><span>17-32 of 12,335 results for</span>
        </h2>
    -->
</div><div id="search-help-content-next" style="display: none;">
    <!--
        <div id="search-help-content"></div>
    -->
</div>
<div id="desktop-auto-sparkle-next" style="display: none;">
    <!--
    <div id="desktop-auto-sparkle">
    </div>
    -->
</div><c:import url="/layouts/DebugInfoPageletLayout1.jsp"></c:import>
<div id="result-info-bar-next" style="display: none;">
    <!--
    <div id="s-result-info-bar" class="a-row a-spacing-base searchUndoAUIHacks"><div id="s-result-info-bar-content" class="a-row"><div class="a-column a-span8 a-spacing-none"><div class="s-first-column">
            <h2 id="s-result-count" class="a-size-base a-spacing-small a-spacing-top-small a-text-normal">17-32 of 12,335 results for <span><span class="a-color-state a-text-bold">&#034;smartphones&#034;</span></span></h2></div>
        </div><div class="a-column a-span4 a-text-right a-spacing-none a-span-last"><div class="a-row a-spacing-micro a-spacing-top-micro"><div class="s-last-column">
                    <div class="a-popover-preload" id="a-popover-department-picker"><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_0?fst=as%3Aoff&amp;rh=n%3A976419031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Electronics</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_11?fst=as%3Aoff&amp;rh=n%3A976392031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Computers &amp; Accessories</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_21?fst=as%3Aoff&amp;rh=n%3A1350380031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Toys &amp; Games</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_24?fst=as%3Aoff&amp;rh=n%3A976389031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Books</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_n_30?fst=as%3Aoff&amp;rh=n%3A1350387031%2Ck%3Asmartphones&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869&amp;rnid=3576079031">Watches</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_32?rh=k%3Asmartphones%2Ci%3Amisc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Everything Else</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_33?rh=k%3Asmartphones%2Ci%3Adigital-text&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Kindle Store</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_34?rh=k%3Asmartphones%2Ci%3Aautomotive&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Car &amp; Motorbike</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_35?rh=k%3Asmartphones%2Ci%3Asporting&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Sports, Fitness &amp; Outdoors</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_36?rh=k%3Asmartphones%2Ci%3Akitchen&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Home &amp; Kitchen</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_37?rh=k%3Asmartphones%2Ci%3Ababy&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Baby</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_38?rh=k%3Asmartphones%2Ci%3Ahpc&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Health &amp; Personal Care</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_39?rh=k%3Asmartphones%2Ci%3Ami&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Musical Instruments</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_40?rh=k%3Asmartphones%2Ci%3Aoffice-products&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Office Products</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_41?rh=k%3Asmartphones%2Ci%3Aluggage&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Luggage &amp; Bags</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_42?rh=k%3Asmartphones%2Ci%3Avideogames&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Video Games</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_43?rh=k%3Asmartphones%2Ci%3Asoftware&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Software</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_44?rh=k%3Asmartphones%2Ci%3Aapparel&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Clothing &amp; Accessories</a></div><div class="a-row a-spacing-micro a-spacing-top-micro"><a class="a-link-normal a-color-base a-nowrap a-text-normal" href="/s/ref=sr_nr_i_45?rh=k%3Asmartphones%2Ci%3Ashoes&amp;keywords=smartphones&amp;ie=UTF8&amp;qid=1431746869">Shoes &amp; Handbags</a></div></div><span class="s-inline-block a-spacing-mini a-spacing-top-mini">
        <span class="a-declarative" data-action="a-popover" data-a-popover="{&quot;name&quot;:&quot;department-picker&quot;,&quot;closeButton&quot;:false}"><a href="javascript:void(0)" class="a-popover-trigger a-declarative"><span class="a-size-base a-color-base">Choose a Department to sort</span><i class="a-icon a-icon-popover"></i></a></span></span>
</div>
            </div></div></div></div>
    -->
</div>
<div id="didYouMean-next" style="display: none;">
    <!--
        <div id="didYouMean"></div>
    -->
</div>
<div id="mp3AlbumsBar-next" style="display: none;">
    <!--
        <div id="mp3AlbumsBar"></div>
    -->
</div>
<div id="quartsPagelet-next" style="display: none;">
    <!--
        <div id="quartsPagelet"></div>
    -->
</div>
<div id="apsRedirectLink-next" style="display: none;">
    <!--
        <div id="apsRedirectLink"></div>
    -->
</div>
<div id="past-purchase-next" style="display: none;">
    <!--
        <div id="past-purchase"></div>
    -->
</div>
<div id="bestRefinement-next" style="display: none;">
    <!--
        <div id="bestRefinement"></div>
    -->
</div>
</div>
            </div>
        </div>

        <div id="staticContent" class="s-span-page">
            <!-- btf pilu -->

  <div style="display: none;">

<div id="nav_browse_flyout" >
  <div id="nav_subcats_wrap" class="nav_browse_wrap">
    <div id="nav_subcats">
      <div id="nav_subcats_0" data-nav-promo-id="kindle"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Kindle E-readers</li><li class="nav_first nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B00KDRQ2RU/ref=nav_shopall_k_ki" class="nav_a nav_item">Kindle</a><div class="nav_tag">A world of books at your fingertips</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B00JG8FHJQ/ref=nav_shopall_k_kp" class="nav_a nav_item">Kindle Paperwhite</a><div class="nav_tag">For the love of reading</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B00IOY5AS6/ref=nav_shopall_k_kp_ki" class="nav_a nav_item">Kindle Voyage</a><div class="nav_tag">Passionately crafted for readers</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/Kindle-Accessories/b/ref=nav_shopall_k_kacce?ie=UTF8&amp;node=1634751031" class="nav_a nav_item">Kindle E-reader Accessories</a><div class="nav_tag">Covers, chargers, sleeves and more</div></li><li class="nav_pop_li nav_browse_cat_head nav_divider_before">Kindle Apps & Resources</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/gp/feature.html/ref=nav_shopall_karl3?ie=UTF8&amp;docId=1000659093" class="nav_a nav_item">Free Kindle Reading Apps</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="https://www.amazon.in:443/gp/redirect.html/ref=nav_shopall_kcr?location=https://read.amazon.in/&amp;token=58913ACCA4D526B43BC6E2C36FA384E9D83BA838&amp;source=standards" class="nav_a nav_item" target="_blank">Kindle Cloud Reader</a><div class="nav_tag">Read your Kindle books in a browser</div></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/feature.html/ref=nav_shopall_adr_app_t1?ie=UTF8&amp;docId=1000721773" class="nav_a nav_item">Appstore for Android</a></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/digital/fiona/manage/ref=nav_shopall_myk" class="nav_a nav_item">Manage Your Content and Devices</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Kindle eBooks</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/ebooks-kindle/b/ref=nav_shopall_kdl_ebkall?ie=UTF8&amp;node=1634753031" class="nav_a nav_item">All Kindle eBooks</a></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/bestsellers/digital-text/1634753031/ref=nav_shopall_kdl_ebkbest" class="nav_a nav_item">eBook Bestsellers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Free-Kindle-eBooks/b/ref=nav_shopall_kdl_ebkfree?ie=UTF8&amp;node=4341284031" class="nav_a nav_item">Free Kindle eBooks</a></li><li class="nav_subcat_link nav_pop_li"><a href="/literature-fiction-ebook-kindle/b/ref=nav_shopall_kdl_ebklitfict?ie=UTF8&amp;node=1637119031" class="nav_a nav_item">Literature & Fiction</a></li><li class="nav_subcat_link nav_pop_li"><a href="/business-finance-ebooks-kindle/b/ref=nav_shopall_kdl_ebkbizeco?ie=UTF8&amp;node=1637021031" class="nav_a nav_item">Business & Economics</a></li></ul></div>
<div id="nav_subcats_1" data-nav-promo-id="amazon-apps"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Amazon Apps</li><li class="nav_first nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.html/ref=nav_shopall_shop_app?ie=UTF8&amp;docId=1000745723" class="nav_a nav_item">Amazon Shopping App</a><div class="nav_tag">Shop on the go anytime, anywhere</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.html/ref=nav_shopall_kindle_app?ie=UTF8&amp;docId=1000659093" class="nav_a nav_item">Free Kindle Reading Apps</a><div class="nav_tag">For PC, iPad, iPhone, Android, and more</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.html/ref=nav_shopall_android_app?ie=UTF8&amp;docId=1000721773" class="nav_a nav_item">Amazon Appstore for Android</a><div class="nav_tag">Get a paid app or game for free</div></li></ul></div>
<div id="nav_subcats_2" data-nav-promo-id="books"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Books</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Books/b/ref=nav_shopall_books_all?ie=UTF8&amp;node=976389031" class="nav_a nav_item">All Books</a></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/bestsellers/books/ref=nav_shopall_books_bestsellers" class="nav_a nav_item">Bestsellers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_sa_menu_bx_nrpo?ie=UTF8&amp;node=4143742031" class="nav_a nav_item">New Releases & Pre-orders</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Hindi-Books/b/ref=nav_shopall_books_hindi?ie=UTF8&amp;node=4506102031" class="nav_a nav_item">Hindi Books</a></li><li class="nav_subcat_link nav_pop_li"><a href="/children-books/b/ref=nav_shopall_books_childrens?ie=UTF8&amp;node=1318073031" class="nav_a nav_item">Children's & Young Adult</a></li><li class="nav_subcat_link nav_pop_li"><a href="/literature-fiction-books/b/ref=nav_shopall_books_lit_fiction?ie=UTF8&amp;node=1318157031" class="nav_a nav_item">Literature & Fiction</a></li><li class="nav_subcat_link nav_pop_li"><a href="/indian-writing/b/ref=nav_shopall_books_indian_writing?ie=UTF8&amp;node=1890195031" class="nav_a nav_item">Indian Writing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Exam-Preparations-Books/b/ref=nav_shopall_sa_menu_books_exam_prep?ie=UTF8&amp;node=4149751031" class="nav_a nav_item">All Exam Preparation</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Text-Books/b/ref=nav_shopall_textbooks?ie=UTF8&amp;node=4149418031" class="nav_a nav_item">All Textbooks</a></li><li class="nav_subcat_link nav_pop_li"><a href="/business-economics-books/b/ref=nav_shopall_books_business?ie=UTF8&amp;node=1318068031" class="nav_a nav_item">Business & Economics</a></li><li class="nav_subcat_link nav_pop_li"><a href="/ebooks-kindle/b/ref=nav_shopall_books_ebooks?ie=UTF8&amp;node=1634753031" class="nav_a nav_item">Kindle eBooks</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/b/ref=nav_shopall_edu_software?ie=UTF8&amp;node=5490084031" class="nav_a nav_item">Educational Software</a></li></ul></div>
<div id="nav_subcats_3" data-nav-promo-id="music-movies-games"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head"> Movies & TV Shows</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/movies-tv-shows/b/ref=nav_shopall_movies_all?ie=UTF8&amp;node=976416031" class="nav_a nav_item">All Movies & TV Shows</a></li><li class="nav_subcat_link nav_pop_li"><a href="/blu-ray/b/ref=nav_shopall_movies_bluray?ie=UTF8&amp;node=1575405031" class="nav_a nav_item">Blu-ray</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Hindi-Movies-TV-Shows/b/ref=nav_shopall_movies_all_eng?ie=UTF8&amp;node=4068583031" class="nav_a nav_item">All English</a></li><li class="nav_subcat_link nav_pop_li"><a href="/English-Movies-TV-Shows/b/ref=nav_shopall_movies_all_hindi?ie=UTF8&amp;node=4068584031" class="nav_a nav_item">All Hindi</a></li><li class="nav_pop_li nav_browse_cat_head nav_divider_before">Video Games</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/video-games/b/ref=nav_shopall_vg_avg?ie=UTF8&amp;node=976460031" class="nav_a nav_item">All Consoles, Games & Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/pc-games/b/ref=nav_shopall_vg_pcg?ie=UTF8&amp;node=1376518031" class="nav_a nav_item"> PC Games </a></li><li class="nav_subcat_link nav_pop_li"><a href="/Video-Games-New-Releases/b/ref=nav_shopall_vg_newfuture?ie=UTF8&amp;node=4069183031" class="nav_a nav_item">Pre-orders & New Releases</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Video-Games-Consoles/b/ref=nav_shopall_vg_consoles?ie=UTF8&amp;node=4092115031" class="nav_a nav_item">Consoles</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Video-Games-Accessories/b/ref=nav_shopall_vg_accessories?ie=UTF8&amp;node=4092116031" class="nav_a nav_item">Accessories</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Music</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/music/b/ref=nav_shopall_music_all?ie=UTF8&amp;node=976445031" class="nav_a nav_item">All Music</a></li><li class="nav_subcat_link nav_pop_li"><a href="/International-Music/b/ref=nav_shopall_music_international?ie=UTF8&amp;node=4092674031" class="nav_a nav_item">International Music</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Film-Songs/b/ref=nav_shopall_music_film_songs?ie=UTF8&amp;node=1375845031" class="nav_a nav_item">Film Songs</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Indian-Classical/b/ref=nav_shopall_music_indian_classical?ie=UTF8&amp;node=1375848031" class="nav_a nav_item">Indian Classical</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Musical-Instruments/b/ref=nav_shopall_musical_inst?ie=UTF8&amp;node=3677697031" class="nav_a nav_item">Musical Instruments</a></li></ul></div>
<div id="nav_subcats_4" data-nav-promo-id="phones-accessories"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Mobiles & Tablets</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/mobiles-accessories/b/ref=nav_shopall_sa_menu_mobile_all_mobiles?ie=UTF8&amp;node=1389401031" class="nav_a nav_item">All Mobile Phones</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Smartphones/b/ref=nav_shopall_sa_menu_mobile_smartphone?ie=UTF8&amp;node=1805560031" class="nav_a nav_item">Smartphones</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Android-Mobiles/b/ref=nav_shopall_sa_menu_mobile_android_mobiles?ie=UTF8&amp;node=4916280031" class="nav_a nav_item">Android Mobiles</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Windows-Mobiles/b/ref=nav_shopall_sa_menu_mobile_windows_mobile?ie=UTF8&amp;node=4916281031" class="nav_a nav_item">Windows Mobiles</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/mobile-phone-accessories/b/ref=nav_shopall_sa_menu_mobile_accessories?ie=UTF8&amp;node=1389402031" class="nav_a nav_item">All Mobile Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Cases-Covers/b/ref=nav_shopall_sa_menu_mobile_covers?ie=UTF8&amp;node=1389409031" class="nav_a nav_item">Cases & Covers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Headsets/b/ref=nav_shopall_sa_menu_mobile_headsets?ie=UTF8&amp;node=1389418031" class="nav_a nav_item">Headsets</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Power-Banks/b/ref=nav_shopall_sa_menu_mobile_powerbank?ie=UTF8&amp;node=4222146031" class="nav_a nav_item">Power Banks</a></li><li class="nav_taglined nav_subcat_link nav_pop_li nav_divider_before"><a href="/electronics/b/ref=nav_shopall_sa_menu_mobile_elec_all?ie=UTF8&amp;node=976419031" class="nav_a nav_item"> All Electronics </a><div class="nav_tag">Discover more products</div></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">&nbsp;</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Tablets/b/ref=nav_shopall_mobile_tablets?ie=UTF8&amp;node=1375458031" class="nav_a nav_item">All Tablets</a></li><li class="nav_subcat_link nav_pop_li"><a href="/tablet-accessories/b/ref=nav_shopall_mobile_tablet_acc?ie=UTF8&amp;node=1375328031" class="nav_a nav_item">Tablet Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Landline-Phones/b/ref=nav_shopall_mobile_landline?ie=UTF8&amp;node=1389490031" class="nav_a nav_item">Landline Phones</a></li></ul></div>
<div id="nav_subcats_5" data-nav-promo-id="computer-accessories"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head"> Computers & Accessories </li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/computers-and-accessories/b/ref=nav_shopall_computers_all?ie=UTF8&amp;node=976392031" class="nav_a nav_item"> All Computers & Accessories </a></li><li class="nav_subcat_link nav_pop_li"><a href="/Laptops/b/ref=nav_shopall_computers_laptop?ie=UTF8&amp;node=1375424031" class="nav_a nav_item">Laptops</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_nav_shopall_computers_desktops?ie=UTF8&amp;node=5208309031" class="nav_a nav_item">Desktops & Monitors</a></li><li class="nav_subcat_link nav_pop_li"><a href="/pen-drive/b/ref=nav_shopall_computers_pen_drives?ie=UTF8&amp;node=1375411031" class="nav_a nav_item">Pen Drives</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Hard-disks/b/ref=nav_shopall_computers_hard_drives?ie=UTF8&amp;node=1375395031" class="nav_a nav_item">Hard Drives</a></li><li class="nav_subcat_link nav_pop_li"><a href="/memory-cards/b/ref=nav_shopall_computers_memory_cards?ie=UTF8&amp;node=1388963031" class="nav_a nav_item">Memory Cards</a></li><li class="nav_subcat_link nav_pop_li"><a href="/printers-scanners/b/ref=nav_shopall_computers_printers?ie=UTF8&amp;node=1575411031" class="nav_a nav_item">Printers & Ink</a></li><li class="nav_subcat_link nav_pop_li"><a href="/networking-devices/b/ref=nav_shopall_computers_networking?ie=UTF8&amp;node=1375427031" class="nav_a nav_item">Networking & Internet Devices</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Computer-Accessories/b/ref=nav_shopall_computers_accessories?ie=UTF8&amp;node=1375248031" class="nav_a nav_item"> Computer Accessories </a></li><li class="nav_subcat_link nav_pop_li"><a href="/Software/b/ref=nav_shopall_software?ie=UTF8&amp;node=976451031" class="nav_a nav_item"> Software </a></li><li class="nav_taglined nav_subcat_link nav_pop_li nav_divider_before"><a href="/electronics/b/ref=nav_shopall_computers_elec_all?ie=UTF8&amp;node=976419031" class="nav_a nav_item"> All Electronics </a><div class="nav_tag">Discover more products</div></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Office & Stationery</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Office-Stationery-Supplies/b/ref=nav_shopall_nav_shopall_office_all?ie=UTF8&amp;node=2454172031" class="nav_a nav_item">All Office & Stationery</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Pens-Writing-Supplies/b/ref=nav_shopall_nav_shopall_office_pens?ie=UTF8&amp;node=3591021031" class="nav_a nav_item">Pens & Writing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Art-Craft-Supplies/b/ref=nav_shopall_nav_shopall_office_art?ie=UTF8&amp;node=3591014031" class="nav_a nav_item">Art & Craft Supplies</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Office-Electronics/b/ref=nav_shopall_nav_shopall_office_electronics?ie=UTF8&amp;node=3591018031" class="nav_a nav_item">Office Electronics</a></li></ul></div>
<div id="nav_subcats_6" data-nav-promo-id="cam-aud-vid"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Cameras &amp; Photography</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/camera-photography/b/ref=nav_shopall_cam_all?ie=UTF8&amp;node=1388977031" class="nav_a nav_item">All Cameras & Photography</a></li><li class="nav_subcat_link nav_pop_li"><a href="/digital-slr-cameras/b/ref=nav_shopall_cam_dslr?ie=UTF8&amp;node=1389177031" class="nav_a nav_item">Digital SLRs</a></li><li class="nav_subcat_link nav_pop_li"><a href="/point-shoot-digital-cameras/b/ref=nav_shopall_cam_pointshoot?ie=UTF8&amp;node=1389181031" class="nav_a nav_item">Point & Shoot Cameras</a></li><li class="nav_subcat_link nav_pop_li"><a href="/camera-lenses/b/ref=nav_shopall_cam_lenses?ie=UTF8&amp;node=1389197031" class="nav_a nav_item">Lenses</a></li><li class="nav_subcat_link nav_pop_li"><a href="/camera-accessories/b/ref=nav_shopall_cam_accessories?ie=UTF8&amp;node=1388978031" class="nav_a nav_item">Camera Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Surveillance-Cameras/b/ref=nav_shopall_cam_surveillance?ie=UTF8&amp;node=1389203031" class="nav_a nav_item">Security & Surveillance</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Binoculars-Telescopes-Optics/b/ref=nav_shopall_cam_binotele?ie=UTF8&amp;node=1389159031" class="nav_a nav_item">Binoculars & Telescopes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/camcorders/b/ref=nav_shopall_cam_camcorder?ie=UTF8&amp;node=1389174031" class="nav_a nav_item">Camcorders</a></li><li class="nav_pop_li nav_browse_cat_head nav_divider_before">Musical Instruments</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Musical-Instruments/b/ref=nav_shopall_musical_instruments_all?ie=UTF8&amp;node=3677697031" class="nav_a nav_item">All Musical Instruments</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_musical_instruments_all?ie=UTF8&amp;node=4581267031" class="nav_a nav_item">Musical Instrument Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_musical_instruments_all?ie=UTF8&amp;node=4581266031" class="nav_a nav_item">Professional Audio & Recording</a></li><li class="nav_taglined nav_subcat_link nav_pop_li nav_divider_before"><a href="/electronics/b/ref=nav_shopall_cam_aud_all_elec?ie=UTF8&amp;node=976419031" class="nav_a nav_item"> All Electronics </a><div class="nav_tag">Discover more products</div></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Audio & Video</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/tv-home-entertainment/b/ref=nav_shopall_aud_vid_all?ie=UTF8&amp;node=1575407031" class="nav_a nav_item">All Audio & Video</a></li><li class="nav_subcat_link nav_pop_li"><a href="/headphones/b/ref=nav_shopall_aud_vid_headphones?ie=UTF8&amp;node=1388921031" class="nav_a nav_item">Headphones</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Speakers/b/ref=nav_shopall_aud_vid_speakers?ie=UTF8&amp;node=1389365031" class="nav_a nav_item">Speakers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Home-Entertainment-Systems/b/ref=nav_shopall_aud_vid_home_ent?ie=UTF8&amp;node=1389375031" class="nav_a nav_item">TV & Home Entertainment</a></li><li class="nav_subcat_link nav_pop_li"><a href="/mp3-media-players/b/ref=nav_shopall_mp3_all?ie=UTF8&amp;node=1389433031" class="nav_a nav_item">MP3 & Media Players</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Home-Audio-Video-Accessories/b/ref=nav_shopall_aud_vid_accessories?ie=UTF8&amp;node=1388878031" class="nav_a nav_item">Audio & Video Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Projectors/b/ref=nav_shopall_aud_vid_projectors?ie=UTF8&amp;node=1389388031" class="nav_a nav_item">Projectors</a></li></ul></div>
<div id="nav_subcats_7" data-nav-promo-id="home-kitchen"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Home & Kitchen </li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Home-Kitchen/b/ref=nav_shopall_sa_menu_hk_all?ie=UTF8&amp;node=976442031" class="nav_a nav_item">All Home & Kitchen</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_hk_kitchen_appliances?ie=UTF8&amp;node=4951860031" class="nav_a nav_item">Kitchen & Home Appliances</a><div class="nav_tag">Induction Cooktops, Irons, Hand Blenders</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/Large-Appliances/b/ref=nav_shopall_nav_shopall_lrgapp?ie=UTF8&amp;node=1380263031" class="nav_a nav_item"> Large Appliances </a><div class="nav_tag">Just Launched</div></li><li class="nav_subcat_link nav_pop_li"><a href="/Kitchen-Dining/b/ref=nav_shopall_hk_kitchendining?ie=UTF8&amp;node=3044927031" class="nav_a nav_item">Kitchen & Dining</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Home-D%C3%A9cor/b/ref=nav_shopall_hk_home_decor?ie=UTF8&amp;node=1380374031" class="nav_a nav_item">Home & Decor</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Home-Furnishing/b/ref=nav_shopall_hk_furnishing?ie=UTF8&amp;node=1380442031" class="nav_a nav_item">Home Furnishing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Indoor-Lighting/b/ref=nav_shopall_hk_lighting?ie=UTF8&amp;node=1380485031" class="nav_a nav_item">Indoor Lighting</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Home-Improvement/b/ref=nav_shopall_hk_homeimprovement?ie=UTF8&amp;node=4286640031" class="nav_a nav_item">Home Improvement</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Lawn-Garden/b/ref=nav_shopall_hk_lawngarden?ie=UTF8&amp;node=4294807031" class="nav_a nav_item">Lawn & Garden</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Pet Supplies</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Pet-Supplies/b/ref=nav_shopall_pets_allpetsupplies?ie=UTF8&amp;node=2454181031" class="nav_a nav_item">All Pet Supplies</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Dogs-Supplies/b/ref=nav_shopall_pets_dogs?ie=UTF8&amp;node=4771342031" class="nav_a nav_item">Dogs</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Cats-Supplies/b/ref=nav_shopall_pets_cats?ie=UTF8&amp;node=4771341031" class="nav_a nav_item">Cats</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Birds-Supplies/b/ref=nav_shopall_pets_birds?ie=UTF8&amp;node=4771340031" class="nav_a nav_item">Birds</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Fish-Aquatics-Supplies/b/ref=nav_shopall_pets_fish?ie=UTF8&amp;node=4771339031" class="nav_a nav_item">Fish & Aquatics</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Small-Animals-Food/b/ref=nav_shopall_pets_smallanimals?ie=UTF8&amp;node=4771347031" class="nav_a nav_item">Small Animals</a></li></ul></div>
<div id="nav_subcats_8" data-nav-promo-id="toys-baby"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Toys & Games</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Toys-Games/b/ref=nav_shopall_toys_all?ie=UTF8&amp;node=1350380031" class="nav_a nav_item">All Toys & Games</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Puzzles/b/ref=nav_shopall_toys_puzzles?ie=UTF8&amp;node=1378470031" class="nav_a nav_item">Puzzles</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Soft-Toys/b/ref=nav_shopall_toys_softtoys?ie=UTF8&amp;node=1378445031" class="nav_a nav_item">Soft Toys</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Die-Cast-Toy-Vehicles/b/ref=nav_shopall_toys_toyvehicles?ie=UTF8&amp;node=1378242031" class="nav_a nav_item">Die-Cast & Toy Vehicles</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Learning-Educational/b/ref=nav_shopall_toys_learning?ie=UTF8&amp;node=1378342031" class="nav_a nav_item">Learning & Education</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Baby Products</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Baby/b/ref=nav_shopall_baby_all?ie=UTF8&amp;node=1571274031" class="nav_a nav_item">All Baby Products</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Diapering-Nappy-Changing/b/ref=nav_shopall_baby_diapers?ie=UTF8&amp;node=1953345031" class="nav_a nav_item">Diapering & Nappy Changing</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/Nursery/b/ref=nav_shopall_baby_nursery?ie=UTF8&amp;node=1953359031" class="nav_a nav_item">Nursery</a><div class="nav_tag">Furniture, Bedding and Room Décor</div></li><li class="nav_subcat_link nav_pop_li"><a href="/Strollers-Prams/b/ref=nav_shopall_baby_strollers?ie=UTF8&amp;node=1953480031" class="nav_a nav_item">Strollers & Prams</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Nursing-Feeding/b/ref=nav_shopall_baby_feeding?ie=UTF8&amp;node=1953448031" class="nav_a nav_item">Nursing & Feeding</a></li></ul></div>
<div id="nav_subcats_9" data-nav-promo-id="sports-outdoors"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Sports, Fitness & Outdoors</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Sports/b/ref=nav_shopall_sports_all?ie=UTF8&amp;node=1984443031" class="nav_a nav_item">All Sports, Fitness & Outdoors</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Exercise-Fitness/b/ref=nav_shopall_sports_fitness?ie=UTF8&amp;node=3403635031" class="nav_a nav_item">Exercise & Fitness</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Camping-Hiking/b/ref=nav_shopall_sports_camping?ie=UTF8&amp;node=1984988031" class="nav_a nav_item">Camping & Hiking</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Cycling/b/ref=nav_shopall_sports_cycling?ie=UTF8&amp;node=3403629031" class="nav_a nav_item">Cycling</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Cricket/b/ref=nav_shopall_sports_cricket?ie=UTF8&amp;node=3403628031" class="nav_a nav_item">Cricket</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Badminton/b/ref=nav_shopall_sports_badminton?ie=UTF8&amp;node=3403619031" class="nav_a nav_item">Badminton</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Swimming/b/ref=nav_shopall_sports_swimming?ie=UTF8&amp;node=3404234031" class="nav_a nav_item">Swimming</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Motorbikes-Accessories/b/ref=nav_shopall_sports_motorbiking?ie=UTF8&amp;node=3414627031" class="nav_a nav_item">Motorbiking Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Golf/b/ref=nav_shopall_sports_golf?ie=UTF8&amp;node=3403644031" class="nav_a nav_item">Golf</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Fanshop/b/ref=nav_shopall_sports_fanshop?ie=UTF8&amp;node=3403636031" class="nav_a nav_item">Fan Shop</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Football/b/ref=nav_shopall_sports_football?ie=UTF8&amp;node=3403640031" class="nav_a nav_item">Football</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Tennis/b/ref=nav_shopall_sports_tennis?ie=UTF8&amp;node=3403670031" class="nav_a nav_item">Tennis</a></li></ul></div>
<div id="nav_subcats_10" data-nav-promo-id="beauty-hpc"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Beauty & Health</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/beauty/b/ref=nav_shopall_beauty_all?ie=UTF8&amp;node=1355016031" class="nav_a nav_item">All Beauty</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_beauty_lux?ie=UTF8&amp;node=5311359031" class="nav_a nav_item">Luxury Beauty</a><div class="nav_tag">Just Launched</div></li><li class="nav_subcat_link nav_pop_li"><a href="/Fragrances/b/ref=nav_shopall_beauty_fragrance?ie=UTF8&amp;node=1374298031" class="nav_a nav_item">Fragrance</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/health-and-personal-care/b/ref=nav_shopall_beauty_health_all?ie=UTF8&amp;node=1350384031" class="nav_a nav_item">All Health</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Diet-Nutrition/b/ref=nav_shopall_hpc_nutrition?ie=UTF8&amp;node=1374489031" class="nav_a nav_item"> Diet & Nutrition</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Personal-Care/b/ref=nav_shopall_beauty_personalcare?ie=UTF8&amp;node=1374594031" class="nav_a nav_item"> Personal Care</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Personal-Care-Appliances/b/ref=nav_shopall_beauty_pca?ie=UTF8&amp;node=3150028031" class="nav_a nav_item">Personal Care Appliances</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Health-Care-Devices/b/ref=nav_shopall_beauty_hcd?ie=UTF8&amp;node=3150027031" class="nav_a nav_item">Health Care Devices</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/b/ref=nav_shopall_beauty_mengrooming?ie=UTF8&amp;node=5122801031" class="nav_a nav_item">Men's Grooming</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Gourmet & Specialty Foods</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Gourmet-Specialty-Foods/b/ref=nav_shopall_gourmet_all?ie=UTF8&amp;node=2454178031" class="nav_a nav_item">All Gourmet & Specialty Foods</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Coffee-Tea-Beverages/b/ref=nav_shopall_gourmet_beverages?ie=UTF8&amp;node=4859478031" class="nav_a nav_item">Coffee, Tea & Beverages</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Snack-Foods/b/ref=nav_shopall_gourmet_snacks?ie=UTF8&amp;node=4859498031" class="nav_a nav_item">Snack Foods</a></li></ul></div>
<div id="nav_subcats_11" data-nav-promo-id="clothing-accessories"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Clothing & Accessories</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Womens-clothing/b/ref=nav_shopall_sa_menu_cloacc_allwomen?ie=UTF8&amp;node=1953602031" class="nav_a nav_item">Women's Clothing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Mens-Clothing/b/ref=nav_shopall_sa_menu_cloacc_allmendenim?ie=UTF8&amp;node=1968024031" class="nav_a nav_item">Men's Clothing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/kids-clothing/b/ref=nav_shopall_sa_menu_cloacc_kids?ie=UTF8&amp;node=4091091031" class="nav_a nav_item">Kids' Clothing</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/womens-intimate-apparel/b/ref=nav_shopall_sa_menu_cloacc_wintimate?ie=UTF8&amp;node=4725138031" class="nav_a nav_item">Women's Intimate Apparel</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Mens-Inner-wear/b/ref=nav_shopall_sa_menu_cloacc_minnerwear?ie=UTF8&amp;node=1968126031" class="nav_a nav_item">Men's Innerwear</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/b/ref=nav_shopall_sa_menu_cloacc_allaccess?ie=UTF8&amp;node=4516623031" class="nav_a nav_item">All Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Clothing-accesories/b/ref=nav_shopall_sa_menu_cloacc_allcloaccess?ie=UTF8&amp;node=1571271031" class="nav_a nav_item">All Clothing & Accessories</a></li></ul></div>
<div id="nav_subcats_12" data-nav-promo-id="watches-jewelry"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head"> Watches </li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Watches/b/ref=nav_shopall_watches_all?ie=UTF8&amp;node=1350387031" class="nav_a nav_item">All Watches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Men-Watches/b/ref=nav_shopall_watches_men?ie=UTF8&amp;node=2563504031" class="nav_a nav_item">Men's Watches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Women-Watches/b/ref=nav_shopall_watches_women?ie=UTF8&amp;node=2563505031" class="nav_a nav_item">Women's Watches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Children-Watches/b/ref=nav_shopall_watches_children?ie=UTF8&amp;node=2563506031" class="nav_a nav_item">Children's Watches</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Sports/b/ref=nav_shopall_watches_sports?ie=UTF8&amp;node=3044924031" class="nav_a nav_item">Sports Watches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Top-Watch-Gifts/b/ref=nav_shopall_watches_gifts?ie=UTF8&amp;node=2631615031" class="nav_a nav_item">Top Watch Gifts</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_sa_menu_watches_deals?ie=UTF8&amp;node=3513518031" class="nav_a nav_item">Deals on Watches</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Jewellery</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Jewellery/b/ref=nav_shopall_jwl_all?ie=UTF8&amp;node=1951048031" class="nav_a nav_item">All Jewellery</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/Precious-Jewellery/b/ref=nav_shopall_jwl_precious?ie=UTF8&amp;node=5210069031" class="nav_a nav_item">Precious Jewellery</a><div class="nav_tag">Just Launched</div></li><li class="nav_subcat_link nav_pop_li"><a href="/Fashion-Jewellery/b/ref=nav_shopall_jwl_fashion?ie=UTF8&amp;node=5210079031" class="nav_a nav_item">Fashion Jewellery</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Imitation-Jewellery/b/ref=nav_shopall_jwl_traditional?ie=UTF8&amp;node=3543375031" class="nav_a nav_item">Traditional Jewellery</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Designer-Jewellery/b/ref=nav_shopall_jwl_designer?ie=UTF8&amp;node=3044925031" class="nav_a nav_item">Designer Jewellery</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Men-Jewellery/b/ref=nav_shopall_jwl_men?ie=UTF8&amp;node=3543376031" class="nav_a nav_item">Men's Jewellery</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Jewellery-Gifts/b/ref=nav_shopall_jwl_gifts?ie=UTF8&amp;node=3588507031" class="nav_a nav_item">Gift Store</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Jewellery-Sale/b/ref=nav_shopall_jwl_deals?ie=UTF8&amp;node=4034692031" class="nav_a nav_item">Sales & Deals</a></li></ul></div>
<div id="nav_subcats_13" data-nav-promo-id="clothing-shoes-luggage"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Handbags & Clutches</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Handbags-Clutches/b/ref=nav_shopall_hbc_all?ie=UTF8&amp;node=1983338031" class="nav_a nav_item">All Handbags & Clutches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Handbags/b/ref=nav_shopall_hbc_handbags?ie=UTF8&amp;node=1983355031" class="nav_a nav_item">Handbags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Clutches/b/ref=nav_shopall_hbc_clutch?ie=UTF8&amp;node=1983350031" class="nav_a nav_item">Clutches</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Totes/b/ref=nav_shopall_hbc_totes?ie=UTF8&amp;node=1983356031" class="nav_a nav_item">Totes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Sling-Bags/b/ref=nav_shopall_hbc_sling?ie=UTF8&amp;node=1983351031" class="nav_a nav_item">Sling Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Messenger-Bags/b/ref=nav_shopall_hbc_messenger?ie=UTF8&amp;node=2917442031" class="nav_a nav_item">Messenger Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_hbc_wallets?ie=UTF8&amp;node=2917497031" class="nav_a nav_item">Women's Wallets</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Designer-Bags/b/ref=nav_shopall_hbc_premium?ie=UTF8&amp;node=4296704031" class="nav_a nav_item">Premium Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Leather-Bags/b/ref=nav_shopall_hbc_leather?ie=UTF8&amp;node=4296709031" class="nav_a nav_item">Leather Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Handbags-Clutches-Sales-Deals/b/ref=nav_shopall_hbc_deals?ie=UTF8&amp;node=4594603031" class="nav_a nav_item">Sales & Deals</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Luggage & Bags</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Luggage-Bags/b/ref=nav_shopall_lug_all?ie=UTF8&amp;node=2454169031" class="nav_a nav_item">All Luggage & Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Backpacks/b/ref=nav_shopall_lug_backpacks?ie=UTF8&amp;node=2917430031" class="nav_a nav_item">Backpacks</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Bags-Briefcases/b/ref=nav_shopall_lug_briefcases?ie=UTF8&amp;node=2917431031" class="nav_a nav_item">Bags & Briefcases</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Laptop-Bags/b/ref=nav_shopall_lug_laptop?ie=UTF8&amp;node=2917441031" class="nav_a nav_item">Laptop Bags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Travel-Duffles/b/ref=nav_shopall_lug_duffles?ie=UTF8&amp;node=2917451031" class="nav_a nav_item">Travel Duffles</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Luggage/b/ref=nav_shopall_lug_suitcases?ie=UTF8&amp;node=2917432031" class="nav_a nav_item">Luggage</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Travel-Accessories/b/ref=nav_shopall_lug_accessories?ie=UTF8&amp;node=2917434031" class="nav_a nav_item">Travel Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_lug_m_wallets?ie=UTF8&amp;node=2917496031" class="nav_a nav_item">Men's Wallets</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_lug_deals?ie=UTF8&amp;node=4238515031" class="nav_a nav_item">Sales & Deals</a></li></ul></div>
<div id="nav_subcats_14" data-nav-promo-id="shoes"  class="nav_browse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Men's Shoes</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Men-Shoes/b/ref=nav_shopall_shoes_mall?ie=UTF8&amp;node=1983518031" class="nav_a nav_item">All Men's Shoes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Men-Formal-Shoes/b/ref=nav_shopall_shoes_mformal?ie=UTF8&amp;node=1983572031" class="nav_a nav_item">Formal Shoes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Sports-Outdoor-Men-Shoes/b/ref=nav_shopall_shoes_msports?ie=UTF8&amp;node=1983519031" class="nav_a nav_item">Sports & Outdoor</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Loafers-Moccasins-Shoes/b/ref=nav_shopall_shoes_mloafer?ie=UTF8&amp;node=1983573031" class="nav_a nav_item">Loafers & Mocassins</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Sneakers-Men/b/ref=nav_shopall_shoes_msneakers?ie=UTF8&amp;node=1983577031" class="nav_a nav_item">Sneakers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Sandals-Floaters/b/ref=nav_shopall_shoes_sandals?ie=UTF8&amp;node=1983571031" class="nav_a nav_item">Sandals & Floaters</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Flip-Flop-Slippers/b/ref=nav_shopall_shoes_mflipflop?ie=UTF8&amp;node=1983575031" class="nav_a nav_item">Flip-flops</a></li><li class="nav_subcat_link nav_pop_li nav_divider_before"><a href="/Kids-Baby-Shoes/b/ref=nav_shopall_shoes_kids?ie=UTF8&amp;node=4091095031" class="nav_a nav_item">Kids' Shoes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Shoe-Care-Accessories/b/ref=nav_shopall_shoes_access?ie=UTF8&amp;node=1983320031" class="nav_a nav_item">Shoe Care & Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Shoes/b/ref=nav_shopall_shoes_all?ie=UTF8&amp;node=1983396031" class="nav_a nav_item">All Shoes</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Women's Shoes</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Women-Shoes/b/ref=nav_shopall_shoes_wall?ie=UTF8&amp;node=1983578031" class="nav_a nav_item">All Women's Shoes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Pumps-Peeptoes/b/ref=nav_shopall_shoes_wpumps?ie=UTF8&amp;node=1983631031" class="nav_a nav_item">Pumps & Peeptoes</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Fashion-Sandals/b/ref=nav_shopall_shoes_wsandals?ie=UTF8&amp;node=1983633031" class="nav_a nav_item">Fashion Sandals</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Casual-Slippers/b/ref=nav_shopall_shoes_wslippers?ie=UTF8&amp;node=1983639031" class="nav_a nav_item">Casual Slippers</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Ballet-Flats/b/ref=nav_shopall_shoes_wballet?ie=UTF8&amp;node=1983627031" class="nav_a nav_item">Ballet Flats</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Sports-Outdoor-Women-Shoes/b/ref=nav_shopall_shoes_wsports?ie=UTF8&amp;node=1983579031" class="nav_a nav_item">Sports & Outdoor</a></li></ul></div>
<div id="nav_subcats_15" data-nav-promo-id="automotive"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav_pop_li nav_browse_cat_head">Car & Motorbike</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/automotive/b/ref=nav_shopall_auto_all?ie=UTF8&amp;node=4772060031" class="nav_a nav_item">All Car & Motorbike</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_auto_car_acc?ie=UTF8&amp;node=5257474031" class="nav_a nav_item">Car Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_auto_parts?ie=UTF8&amp;node=5257478031" class="nav_a nav_item">Motorbike Accessories & Parts</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_auto_care?ie=UTF8&amp;node=5257472031" class="nav_a nav_item">Car & Motorbike Care</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b/ref=nav_shopall_auto_car_parts?ie=UTF8&amp;node=5257475031" class="nav_a nav_item">Car Parts</a></li></ul></div>

    </div>
    <div class="nav_subcats_div"></div>
    <div class="nav_subcats_div nav_subcats_div2"></div>
  </div>
  <div id="nav_cats_wrap" class="nav_browse_wrap">
    <ul id="nav_cats" class="nav_browse_ul">
      <li class="nav_first nav_taglined nav_pop_li nav_cat" id="nav_cat_0">Kindle E-readers & Books<div class="nav_tag">E-readers and eBooks</div></li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_1">Amazon Apps<div class="nav_tag">Shopping, Kindle, Appstore</div></li><li class="nav_pop_li nav_cat nav_divider_before" id="nav_cat_2">Books</li><li class="nav_pop_li nav_cat" id="nav_cat_3">Movies, Music & Video Games</li><li class="nav_pop_li nav_cat" id="nav_cat_4">Mobiles & Tablets</li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_5"> Computers & Accessories <div class="nav_tag">Just Launched: Software</div></li><li class="nav_pop_li nav_cat" id="nav_cat_6">Cameras, Audio & Video</li><li class="nav_pop_li nav_cat" id="nav_cat_7">Home, Kitchen & Pets</li><li class="nav_pop_li nav_cat" id="nav_cat_8">Toys & Baby Products</li><li class="nav_pop_li nav_cat" id="nav_cat_9">Sports, Fitness & Outdoors</li><li class="nav_pop_li nav_cat" id="nav_cat_10">Beauty, Health & Gourmet</li><li class="nav_pop_li nav_cat" id="nav_cat_11">Clothing & Accessories</li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_12">Watches & Jewellery<div class="nav_tag">Just Launched: Precious Jewellery</div></li><li class="nav_pop_li nav_cat" id="nav_cat_13">Handbags & Luggage</li><li class="nav_pop_li nav_cat" id="nav_cat_14">Shoes</li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_15">Car & Motorbike<div class="nav_tag">Just Launched</div></li><li class="nav_last nav_pop_li nav_no_cat nav_divider_before nav_a_carat" id="nav_cat_16"><span class="nav_a_carat">&rsaquo;</span><a href="/gp/site-directory/ref=nav_shopall_fullstore" class="nav_a">Full Store Directory</a></li>
    </ul>
    <div id="nav_cat_indicator" class="nav-sprite"></div>
  </div>
</div>



















<div id="nav_your_account_flyout" class="nav-flyout-content">
  <ul class="nav_pop_ul">
    <li class="nav_pop_li nav_divider_after" id="nav-ya-btn-signin"><div id="nav-flyout-ya-signin"><a href="https://www.amazon.in/ap/signin?_encoding=UTF8&amp;openid.assoc_handle=inflex&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&amp;openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_signin" rel="nofollow" class="nav-action-button" data-nav-role="signin" data-nav-ref="nav_signin"><span class="nav-action-inner">
      Sign in
    </span></a><div id="nav-flyout-ya-newCust" class="nav_pop_new_cust">
    New customer?
    <a href="https://www.amazon.in/ap/register?_encoding=UTF8&amp;openid.assoc_handle=inflex&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&amp;openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust" rel="nofollow" class="nav_a">
      Start here.
    </a></div></div></li>
<li class="nav_first nav_pop_li"><a href="https://www.amazon.in/gp/css/homepage.html/ref=nav_topnav_ya" class="nav_a">Your Account</a></li><li class="nav_pop_li"><a href="https://www.amazon.in/gp/css/order-history/ref=nav_gno_yam_yrdrs" class="nav_a" id="nav_prefetch_yourorders">Your Orders</a></li><li class="nav_pop_li"><a href="/gp/registry/wishlist/ref=nav_gno_listpop_wi?ie=UTF8&amp;requiresSignIn=1" class="nav_a">Your Wish List</a></li><li class="nav_pop_li"><a href="/gp/yourstore/ref=nav_gno_recs" class="nav_a">Your Recommendations</a></li><li class="nav_last nav_pop_li nav_divider_before"><a href="/gp/digital/fiona/manage/ref=nav_gno_myk" class="nav_a">Manage Your Content and Devices</a></li>  </ul>
  <!--[if IE ]>
    <div class='nav-ie-min-width' style='width: 160px; height: 1px;'></div>
  <![endif]-->
</div>

















<div id="nav-cart-flyout" class="nav-empty nav-flyout-content"
  data-one="" data-many=""><div class="nav-dynamic-full"><div id="nav-cart-standard" class='nav-cart-content'><a href="/gp/cart/view.html/ref=nav_flyout_viewcart?ie=UTF8&amp;hasWorkingJavascript=1" class='nav-cart-title'></a><div class='nav-cart-subtitle'></div><div class='nav-cart-items'></div></div><div id='nav-cart-pantry' class='nav-cart-content'
      data-box="" data-boxes=""
      data-box-filled="" data-boxes-filled=""><a href="/gp/cart/view.html/ref=nav_flyout_viewcart?ie=UTF8&amp;hasWorkingJavascript=1" class='nav-cart-title'></a><div class='nav-cart-subtitle'></div><div class='nav-cart-items'></div></div></div><div class='nav-ajax-message'></div><div class='nav-dynamic-empty'><p class='nav_p nav-bold nav-cart-empty'> Your Shopping Cart is empty.</p><p class='nav_p '> Give it purpose&mdash;fill it with books, movies, mobiles, cameras, toys and fashion jewellery.</p><p class='nav_p '> If you already have an account, <a href="https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_signin_cart" class="nav_a">sign in</a>.</p></div><div class='nav-ajax-error-msg'><p class='nav_p nav-bold'> There's a problem previewing your cart right now.</p><p class='nav_p '> Check your Internet connection and <a href="/gp/cart/view.html/ref=nav_flyout_viewcart?ie=UTF8&hasWorkingJavascript=1" class="nav_a">go to your cart</a>, or <a href='javascript:void(0);' class='nav_a nav-try-again'>try again</a>.</p></div><div id='nav-cart-footer'><a href="/gp/cart/view.html/ref=nav_flyout_viewcart?ie=UTF8&amp;hasWorkingJavascript=1" id="nav-cart-menu-button" class="nav-action-button"><span class="nav-action-inner">
        View Cart
        <span id='nav-cart-menu-button-count' ><span id='nav-cart-zero'>(<span class='nav-cart-count'>0</span> items)</span><span id='nav-cart-one' style='display: none;'>(<span class='nav-cart-count'>0</span> item)</span><span id='nav-cart-many' style='display: none;'>(<span class='nav-cart-count'>0</span> items)</span></span></span></a></div></div>











<div id="nav_wishlist_flyout" class="nav-empty nav-flyout-content">
  <div class='nav-ajax-message'></div>
  <ul class='nav_dynamic nav_pop_ul nav_divider_after'></ul>
  <ul class="nav_pop_ul">
    <li class="nav_first nav_pop_li nav-dynamic-empty"><a href="/gp/registry/wishlist/ref=nav_wishlist_gno_createwl?ie=UTF8&amp;triggerElementID=createList" class="nav_a">Create a Wish List</a></li><li class="nav_pop_li"><a href="/gp/registry/search.html/ref=nav_wishlist_gno_listpop_find?ie=UTF8&amp;type=wishlist" class="nav_a">Find a Wish List</a></li><li class="nav_last nav_taglined nav_pop_li"><a href="/wishlist/universal/ref=nav_wishlist_gno_listpop_uwl" class="nav_a">Wish from Any Website</a><div class="nav_tag">Add items to your List from anywhere</div></li>
  </ul>
</div>













<div id="nav-signin-tooltip"><a href="https://www.amazon.in/ap/signin?_encoding=UTF8&amp;openid.assoc_handle=inflex&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&amp;openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_signin" class="nav-action-button" data-nav-role="signin" data-nav-ref="nav_custrec_signin"><span class="nav-action-inner">
      Sign in
    </span></a><div class="nav-signin-tooltip-footer">
    New customer? <a href="https://www.amazon.in/ap/register?_encoding=UTF8&amp;openid.assoc_handle=inflex&amp;openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&amp;openid.mode=checkid_setup&amp;openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&amp;openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&amp;openid.pape.max_auth_age=0&amp;openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_custrec_newcust" class="nav-a">
      Start here.
    </a></div></div>











<script type='text/html' id='nav-tpl-discoveryPanelList'><# var renderItems = function(items) { #>    <span class='nav-dp-title nav-item'>            </span>     <# jQuery.each(items, function (i, item) { #>        <div class='nav-divider nav-item'></div>        <span class='nav-item'>            <a href='<#=item.order_link#>' class='nav-dp-link'>                    <span class='nav-dp-left-column'>                        <img src='<#=item.image#>' class='nav-dp-image'/>                    </span>                    <span class='nav-dp-right-column'>                        <span class='nav-dp-text <#=item.status#>'>                            <#=item.status_text#>                            <br/>                        </span>                        <# if(item.secondary_status_text) { #>                            <span class='nav-dp-text-secondary <#=item.status#>'>                                <#=item.secondary_status_text#>                            </span>                        <# } #>                    </span>            </a>        </span>  <# }); #>  <div class='nav-divider nav-item'></div>  <a href="/your-orders/ref=nav_dp_yourorder" class="nav-dp-link-emphasis">        </a><# }; #><# renderItems(items); #></script><script type='text/html' id='nav-tpl-asin-promo'><a href='<#=destination #>' class='nav_asin_promo'>  <img src='<#=image #>' class='nav_asin_promo_img'/>  <span class='nav_asin_promo_headline'><#=headline #></span>  <span class='nav_asin_promo_info'>    <span class='nav_asin_promo_title'><#=productTitle #></span>    <span class='nav_asin_promo_title2'><#=productTitle2 #></span>    <span class='nav_asin_promo_price'><#=price #></span>  </span>  <span class='nav_asin_promo_button nav-sprite'><#=button #></span></a></script><script type='text/html' id='nav-tpl-itemList'><# var hasColumns = (function () {  var checkColumns = function (_items) {    if (!_items) {      return false;    }    for (var i=0; i<_items.length; i++) {      if (_items[i].columnBreak || (_items[i].items && checkColumns(_items[i].items))) {        return true;      }    }    return false;  };  return checkColumns(items);}()); #><# if(hasColumns) { #>  <div class='nav-column nav-column-first'><# } #><# var renderItems = function(items) { #>  <# jQuery.each(items, function (i, item) { #>    <# if(hasColumns && item.columnBreak) { #>      </div><div class='nav-column nav-column-notfirst'>    <# } #>    <# if(item.dividerBefore) { #>      <div class='nav-divider'></div>    <# } #>    <# if(item.text || item.content) { #>      <# if(item.url) { #>        <a href='<#=item.url #>' class='nav-link      <# } else {#>        <span class='      <# } #>      <# if(item.panelKey) { #>        nav-hasPanel      <# } #>      <# if(item.items) { #>        nav-title      <# } #>      <# if(item.decorate == 'carat') { #>        nav-carat      <# } #>      nav-item'      <# if(item.extra) { #>        <#=item.extra #>      <# } #>      <# if(item.id) { #>        id='<#=item.id #>'      <# } #>      <# if(item.panelKey) { #>        data-nav-panelkey='<#=item.panelKey #>'      <# } #>      <# if(item.subtextKey) { #>        data-nav-subtextkey='<#=item.subtextKey #>'      <# } #>      <# if(item.image && item.image.height > 16) { #>        style='line-height:<#=item.image.height #>px;'      <# } #>      >      <# if(item.decorate == 'carat') { #>        <i class="nav-icon"></i>      <# } #>      <# if(item.image && item.image.src) { #>        <img class='nav-image' src='<#=item.image.src #>' style='height:<#=item.image.height #>px; width:<#=item.image.width #>px;' />      <# } #>      <# if(item.text) { #>        <span class='nav-text'><#=item.text#></span>      <# } else if (item.content) { #>        <span class='nav-content'><# jQuery.each(item.content, function (j, cItem) { #><# if(cItem.url && cItem.text) { #><a href='<#=cItem.url #>' class='nav-a'><#=cItem.text #></a><# } else if (cItem.text) { #><#=cItem.text#><# } #><# }); #></span>      <# } #>      <# if(item.subtext) { #>        <span class='nav-subtext'><#=item.subtext #></span>      <# } #>      <# if(item.url) { #>        </a>      <# } else {#>        </span>      <# } #>    <# } #>    <# if(item.items) { #>      <div class='nav-panel'> <# renderItems(item.items); #> </div>    <# } #>  <# }); #><# }; #><# renderItems(items); #><# if(hasColumns) { #>  </div><# } #></script><script type='text/html' id='nav-tpl-notificationsList'><div class='nav-item nav-title'>  </div><# jQuery.each(items || [], function (i, item) { #>  <div class='nav-item<# if (item.type) { #> nav-noti-list-<#= item.type #><# } #><# if (item.image && item.image.src) { #> nav-noti-list-with-image<# } #>'>    <# if (item.dismissId) { #>      <div class='nav-noti-list-x' data-noti-id='<#= item.dismissId #>'>&times;</div>    <# } #>    <# if (item.image && item.image.src) { #>      <div class='nav-noti-list-image'>        <img class='nav-noti-list-image-tag' src='<#= item.image.src #>' <# if (item.image.alt) { #> alt='<#= item.image.alt #>'<# } #> <# if (item.image.title) { #> title='<#= item.image.title #>'<# } #>/>      </div>    <# } #>    <# if (item.heading) { #>      <div class='nav-noti-list-heading'><#= item.heading #></div>    <# } #>    <# jQuery.each(item.content || [], function (j, itemContent) { #>      <# if (itemContent.url) { #>        <a href='<#= itemContent.url #>' class='nav-noti-list-content'>      <# } else { #>        <div class='nav-noti-list-content'>      <# } #>        <# if (itemContent.text) { #>          <span class='nav-noti-list-text'><#= itemContent.text #></span>        <# } #>        <# if (itemContent.subtext) { #>          <span class='nav-noti-list-subtext'><#= itemContent.subtext #></span>        <# } #>      <# if (itemContent.url) { #>        </a>      <# } else { #>        </div>      <# } #>    <# }); #>  </div><# }); #></script><script type='text/html' id='nav-tpl-htmlList'>  <# jQuery.each(items, function (i, item) { #>    <div class='nav-item'>      <#=item #>    </div>  <# }); #></script><script type='text/html' id='nav-tpl-wishlist'><# jQuery.each(wishlist, function (i, item) { #>  <li class='nav_pop_li'>    <a href='<#=item.url #>' class='nav_a'>      <#=item.name #>    </a>    <div class='nav_tag'>      <!-- TODO this logic should now be in dynamic-wish-list.mi -->      <# if(typeof item.count !='undefined') { #>        <#=          (item.count == 1 ? "{count} item" : "{count} items")            .replace("{count}", item.count)        #>      <# } #>    </div>  </li><# }); #></script><script type='text/html' id='nav-tpl-subnav'><# if (obj && obj.type === 'vertical') { #>  <# jQuery.each(obj.rows, function (i, row) { #>    <# if (row.flyoutElement === 'button') { #>      <div class='nav_sv_fo_v_button' <#=(row.elementStyle ? 'style="' + row.elementStyle  + '"' : '') #>>        <a href='<#=row.url #>' class='nav-action-button nav-sprite'>          <#=row.text #>        </a>      </div>    <# } else if (row.flyoutElement === 'list' && row.list) { #>      <# jQuery.each(row.list, function (j, list) { #>        <div class="nav_sv_fo_v_column <#=(j === 0) ? 'nav_sv_fo_v_first' : '' #>">          <ul class='<#=list.elementClass #>'>          <# jQuery.each(list.linkList, function (k, link) { #>            <# if (k === 0) { link.elementClass += ' nav_sv_fo_v_first'; } #>            <li class='<#=link.elementClass #>'>              <# if (link.url) { #>                <a href='<#=link.url #>' class='nav_a'><#=link.text #></a>              <# } else { #>                <span class="nav_sv_fo_v_span"><#=link.text #></span>              <# } #>            </li>          <# }); #>          </ul>        </div>      <# }); #>    <# } else if (row.flyoutElement === 'link') { #>      <# if (row.topSpacer) { #>        <div class="nav_sv_fo_v_clear"></div>      <# } #>      <div class='<#=row.elementClass #>'>        <a href='<#=row.url #>' class='nav_sv_fo_v_lmargin nav_a'>          <#=row.text #>        </a>      </div>    <# } #>  <# }); #><# } else if (obj) { #>  <div class='nav_sv_fo_scheduled'>    <#= obj #>  </div><# } #></script><script type='text/html' id='nav-tpl-cart'><# jQuery.each(items, function (i, item) { #>  <div class='nav-cart-item'>    <a href='<#=item.url #>' class='nav-cart-item-link'>      <img src='<#=item.img #>' class='nav-cart-item-image' />      <span class='nav-cart-item-title'><#=item.name #></span>      <# if (item.weight) { #>        <span class='nav-cart-item-weight' style='display:none;'>          <#= "".replace("{value}", item.weight.value).replace("{unit}", item.weight.unit) #>        </span>      <# } #>      <# if (item.ourPrice) { #>        <span class='nav-cart-item-buyingPrice'><#=item.ourPrice #></span>      <# } #>      <# if (item.scarcityMessage) { #>        <span class='<#=item.scarcityClass #>'><#=item.scarcityMessage #></span>      <# } #>      <span class='nav-cart-item-quantity'>        <# if(typeof item.wireless !== 'undefined') { #>          <#= "Items: {count}".replace("{count}", item.qty) #>        <# } else { #>          <#= "Quantity: {count}".replace("{count}", item.qty) #>        <# } #>      </span>    </a>  </div>  <# if (i%2==1) { #>    <div class='nav-cart-item-break'></div>  <# } #><# }); #><div class='nav-cart-item-break'></div></script>



























  </div>
  <script type='text/javascript'>
      window.$Nav && $Nav.declare('config.prefetchUrls', ["https://images-na.ssl-images-amazon.com/images/G/01/authportal/common/images/amznbtn-sprite03._V395592492_.png","https://images-na.ssl-images-amazon.com/images/G/31/authportal/common/images/amazon_logo_no-org_mid._V377570192_.png","https://images-na.ssl-images-amazon.com/images/G/31/authportal/flex/reduced-nav/ap-flex-reduced-nav-2.0._V309255176_.js","https://images-na.ssl-images-amazon.com/images/G/31/authportal/flex/reduced-nav/ap-flex-reduced-nav-2.1._V343893441_.css","https://images-na.ssl-images-amazon.com/images/G/31/gno/sprites/global-sprite-v1._V333157339_.png","https://images-na.ssl-images-amazon.com/images/G/31/x-locale/common/buttons/sign-in-secure._V138348554_.gif","https://images-na.ssl-images-amazon.com/images/G/31/x-locale/common/login/fwcim._V342129342_.js","https://images-na.ssl-images-amazon.com/images/G/31/x-locale/common/transparent-pixel._V386942716_.gif"]);
window.$Nav && $Nav.declare('config.prefetch',function() {
    var pUrls = window.$Nav.getNow('config.prefetchUrls');
    if (window.amznJQ) amznJQ.addPL(pUrls);
    else if (window.P) P.when('A').execute(function (A) { A.preload(pUrls); });
});

  /* nav-config-asset-injection IN::desktop::standard::49573:C&42994:T1&42980:C::isSecure=0::preload navc-avVq5bhn0/FQodEHMA5jytN9MygCd+VsfZRylZmafc3IKajD8vm31liysQkNaIGs rid-1HK5ENCX7F1AFC27P657 seq-776 (Sat May 16 02:16:20 2015) **CACHED-BY-NCCC** */

  __auiPreloadIndex = window.__auiPreloadIndex || 0;
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('A').execute("auiPreloadJS_"+(++__auiPreloadIndex), function(A){
    A.preload("http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavAuiAssets-a34aa87bb465b562264bb7662feb97e6f357dca0.min._V2_.js");
    A.preload("https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/NavAuiAssets-a34aa87bb465b562264bb7662feb97e6f357dca0.secure.min._V2_.js");
    A.preload("http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavMetaAsset-bdbf725d2dcb9712aa9253bc09af97731b74148f._V2_.js");
    A.preload("https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/NavMetaAsset-bdbf725d2dcb9712aa9253bc09af97731b74148f._V2_.js");
  });
  (window.AmazonUIPageJS ? AmazonUIPageJS : P).when('A').execute("auiPreloadCSS_"+(++__auiPreloadIndex), function(A){
    A.preload("http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavAuiAssets-4c6327e530fbf6448291efaf91a613db0dd48b96.min._V2_.css");
    A.preload("https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/NavAuiAssets-4c6327e530fbf6448291efaf91a613db0dd48b96.secure.min._V2_.css");
    A.preload("http://z-ecx.images-amazon.com/images/G/01/AUIClients/NavMetaAsset-fa7f4967b0f2d023988c5d05762ecf8e9c981e87._V2_.css");
    A.preload("https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/NavMetaAsset-fa7f4967b0f2d023988c5d05762ecf8e9c981e87._V2_.css");
  });


  if (window.amznJQ && (typeof window.P !== "object" || !P.AUI_BUILD_DATE)) {
    AmazonUIPageJS.register("A",function(){
      return {"preload":amznJQ.addPL};
    });
  }

    window.$Nav && $Nav.declare('config.flyoutURL', null);
    window.$Nav && $Nav.declare('btf.lite');
    window.amznJQ && amznJQ.declareAvailable('navbarBTFLite');
    window.$Nav && $Nav.declare('btf.full');
    window.$Nav && $Nav.declare('btf.exists');
    window.amznJQ && amznJQ.declareAvailable('navbarBTF');
    (window.AmazonUIPageJS ? AmazonUIPageJS : P).register('navCF');
  </script>

<!-- btf tilu -->


<div id="startingSearchHtmlSkeleton" style="display:none;">
<!--
<div id="main" skeleton-key="results--searchTemplate listLayout so_in_en--left-nav--shopping-engine" class="nav_redesign s-left-nav-rib-redesign" data-app="gp/search" data-page="results" data-page-construction="auisearch">
    <div id="topStatic"></div>
    <div id="top">
        <div id='sprGradient' class='srSprite spr_gradient'>&nbsp;</div>
    </div>
    <div id="searchTemplate" class="searchTemplate listLayout so_in_en">
        <div id="topDynamicContent"></div>
        <div id="rightContainerATF">
            <div id="rightResultsATF">
                <div id="widthPreserver"></div>
                <div id="center"></div>
                <div id="js-boot-btf"></div>
                <div id="centerBelow"></div>
                <div id="centerBelowExtra">
                    <div id="centerBelowExtra1"></div>
                    <div id="centerBelowExtraSponsoredLinks"></div>
                    <div id="centerBelowExtraHowsMySearch"></div>
                    <div id="centerBelowExtra2"></div>
                    <div id="centerBelowExtra3"></div>
                </div>
            </div>
        </div>

        <div id="leftNav">
            <div id="leftNavPrefix"></div>
            <div id="leftNavContainer" style="visibility:hidden"></div> <div id="leftNavPostfix"></div>
            <div id="leftNavAdvertising"></div>
        </div>
        <div id="js-boot-leftnav"></div>
        <div id="ajaxData"></div>

        <div id="js-boot-final"></div>
    </div>
</div>


-->
</div>
<script>
!function() {
  amzn.sx.utils.jsDepMgr.when('jQuery', "search-html-skeleton-installer", function($) {

    var skeleton = $('#startingSearchHtmlSkeleton').html();
    skeleton = skeleton.replace(/^\s*<!--\s*/, '').replace(/\s*-->\s*$/, '');
    amzn.sx.utils.jsDepMgr.when('search-ajax', "search-html-skeleton-installer-runner", function() {
      if (!$.searchAjax) {
        return;
      }


    var skeletonKey = skeleton.match(/^\s*<div.*skeleton-key\s*=\s*\\?"([^"]*)\\?"/i);
    if (skeletonKey)
    {
        $.searchAjax.storeSearchSkeleton(skeletonKey[1], skeleton);
    }

  });

  });
}();
</script>
<script type="text/javascript">
  amzn.sx.utils.jsDepMgr.when('jQuery', 'search-trackingInfo-init', function($) {
    $.pageContext = {"isUnsupportedRequest":true,"isApplicationFailure":false,"rid":"0X849WPJZKXMCE756NPF","qid":"1431746869","pageStructure":"results","pageApp":"gp/search","baseRH":"i%3Aaps%2Ck%3Asmartphones","browseLadder":"i%3Aaps","searchKeywords":"smartphones","searchAlias":"aps","searchAliasDisplayName":"All Departments","csrfToken":"O7z3l4sPQBC0Zsj1crqQ9g+ZI5Qk5bNc97n7RB5g7Rc","searchSkeletonKey":"results--searchTemplate listLayout so_in_en--left-nav--shopping-engine","pageType":"Search","subPageType":"SASKeywordAllProducts","store":"gateway"};
  });
</script>
<script type="text/javascript">
    amzn.sx.utils.jsDepMgr.when('jQuery', '', function($) {

    });


      amzn.sx.utils.jsDepMgr.when('jQuery search-ajax', 'searchAjax-bootstrap-before-ready', function() {});
      amzn.sx.utils.jsDepMgr.when('jQuery search-ajax ready', 'searchAjax-bootstrap-ready', function($) {  // must execute after DOM is ready


        if (!$.searchAjax) {
        	return;
        }

        if ($.searchAjax.isInitialized()) {
          return;
        }

        $.searchAjax.init({

          "pagn": 1,
          "eb": 1,
          "sort": 1,
          "leftNav": 1,

          "keyword": 1,
          "iss": 1,

          "issMin": 8,

          "issCount": 1,

          "predictionLimit": 3,

          "searchHistory": ["smartphones"],

          "ladderMap" : {"shoes":"n:1571283031","grocery":"n:2454178031","everyday-essentials":"n:5756143031","stripbooks":"n:976389031","dvd":"n:976416031","sporting":"n:1984443031","luggage":"n:2454169031","jewelry":"n:1951048031","beauty":"n:1355016031","kitchen":"n:976442031","hpc":"n:1350384031","apparel":"n:1571271031","automotive":"n:4772060031","computers":"n:976392031","software":"n:976451031","gift-cards":"n:3704982031","pets":"n:2454181031","popular":"n:976445031","toys":"n:1350380031","office-products":"n:2454172031","baby":"n:1571274031","videogames":"n:976460031","watches":"n:1350387031","mi":"n:3677697031","digital-text":"n:1571277031","electronics":"n:976419031"},
          "ueClickTime": 1,

          cp: {
            limit: 6,
            time: 0
          },

          entryPause: {
            limit: 3,
            time: 800,
            keyMin: 8
          },

          "phEventQueueing" : 1,

          "intReq" : 0,
          "initRid" :'0X849WPJZKXMCE756NPF',
          "atfTimeout" : 12000,
          "clientLoggingEnabled" : 0,
          "defaultSort" : '',
          "node" : '976454031',
          "pageTimeout" : 12000,
          "preloadType": '0',
          "rootNode" : '',

          "searchAlias" : 'aps',
          "streamDelimiter" : "-&-&-&",
          "tabID" : 'gateway',
          "gurupaAjaxAllowed" : 0,
          "useIFrameForAJAX" : 0,
          "dedupePredictiveATF" : 0,
          "ajaxOnCrossAppPage": 0,
          "appDiv": '#main',

          "useMouseDownPrediction": 1,

          "useNewStripFunc": 1,
          "useNewQidLogging": 1

        });
      });
    </script>
</div>

        <div id="footer" class="s-span-page">
            <script>
P.when('jQuery', 'search-page-utilities', 'search-csl', 'ready').execute('sx:aps-deep-pagination-please-refine-prompt:outer', function($, spUtils, csl) {
$Nav.when('nav.createFlyout').run('sx:aps-deep-pagination-please-refine-prompt:inner', function(createFlyout) {
    csl.init('Search', '0X849WPJZKXMCE756NPF');

    var cnt = 0;
    function executeApsDeepPaginationPleaseRefinePrompt() {
        var prompt, curSearch = location.hash || location.search || '';
        if (($.pageContext.baseRH !== (encodeURIComponent('i:aps,k:') + $.pageContext.searchKeywords)) ||
            ((curSearch.match(/&page=(\d+)&/i) || [])[1] !== "4")) {
            return;
        }

        csl.updateRid(window.ue.rid);
        csl.addWlt('49407');


    }
    spUtils.afterEvent('spATFEvent', executeApsDeepPaginationPleaseRefinePrompt);
})
});
</script>
<script>
P.when('jQuery', 'search-page-utilities', 'search-csl', 'ready').execute('sx:refined-search-deep-pagination-try-aps-prompt:outer', function($, spUtils, csl) {
$Nav.when('nav.createFlyout').run('sx:refined-search-deep-pagination-try-aps-prompt:inner', function(createFlyout) {
    csl.init('Search', '0X849WPJZKXMCE756NPF');

    var cnt = 0;
    function executeRefinedSearchDeepPaginationTryApsPrompt() {
        var prompt, curSearch = location.hash || location.search || '';
        if (($.pageContext.baseRH === (encodeURIComponent('i:aps,k:') + $.pageContext.searchKeywords)) ||
            ((curSearch.match(/&page=(\d+)&/i) || [])[1] !== "4")) {
            return;
        }

        csl.updateRid(window.ue.rid);
        csl.addWlt('50675');


    }
    spUtils.afterEvent('spATFEvent', executeRefinedSearchDeepPaginationTryApsPrompt);
})
});
</script>
<div id="raw-sitewide-rhf" class="searchUndoAUIHacks">







































<style type="text/css">
#rhf_table {
    border: 1px solid #DDD;
    border-radius: 5px;
    border-collapse: separate;
    width: 100% !important;
}

#rhf_container {
    margin-top: 0px;
}

#rhf_container .rhf-sign-in-button {
    margin-bottom: 17px;
}

.rhf_header {
    text-align:left;
    padding:10px 10px 0 10px;
    white-space: nowrap;
}

#rhfMainHeading {
    font-family: Arial;
    font-weight: bold;
    font-size: 18px;
    color: #E47911;
}

.rhf-box-tl {
    background-position: 0px 0px;
    background-repeat:no-repeat;
}
.rhf-box-tc {
    background-position: 0px -41px;
    background-repeat:repeat-x;
}
.rhf-box-tr {
    background-position: 0px -81px;
    background-repeat:no-repeat;
}
.rhf-box-l {
    background-position: -7px 0px;
    background-repeat:repeat-y;
}
.rhf-box-r {
    background-position: 9px 0px;
    background-repeat:repeat-y;
}
.rhf-box-br {
    background-position: 0px -123px;
    background-repeat:no-repeat;
}
.rhf-box-bc {
    background-position: 0px -139px;
    background-repeat:repeat-x;
}
.rhf-box-bl {
    background-position: 0px -158px;
    background-repeat:no-repeat;
}
.rhfHistoryWrapper {
    padding: 0 10px;
}


.rhf_loading_outer {
    height: 248px;
    overflow: hidden;
    position: relative;
    margin-top: 10px;
    width: 100% !important;
}
.rhf_loading_outer[class] {
    display: table;
    position: static;
}
.rhf_loading_middle {
    height: 100%;
    width: 100% !important;
}
.rhf_loading_inner {
    text-align: center;
    vertical-align: middle;
}







/* auiTestSprite is a replacement for swSprite - same image class names apply so we have to wrap the shoveler in a test only class */
#rhfShovelerWrapper .auiTestWrapper .auiTestSprite {
     display: inline-block;
     overflow: hidden;
     padding: 0;
     position: relative;
     vertical-align: middle;
}

#rhfShovelerWrapper .auiTestWrapper .auiTestSprite span {
     left: -9999px;
     position: absolute;
}

#rhfShovelerWrapper .auiTestSprite {
     background: url("http://g-ecx.images-amazon.com/images/G/31/nav2/images/sprite-carousel-btns-stars._V343671889_.png") no-repeat scroll 0 0 transparent;
}

/* Back button and a tag around it */
#rhfShovelerWrapper .auiTestWrapper .shoveler a.back-button,
#rhfShovelerWrapper .auiTestWrapper .shoveler a.next-button {
     width: 36px;
     height: 39px;
     margin-top: 60px;
}

#rhfShovelerWrapper .auiTestWrapper .auiTestSprite.s_shvlBack {
     width: 36px;
     height: 39px;
     background-position: 0 0;
}

#rhfShovelerWrapper .auiTestWrapper .auiTestSprite.s_shvlBack:hover {
     background-position: 0 -54px;
}

#rhfShovelerWrapper .auiTestWrapper .depressed .auiTestSprite.s_shvlBack {
     background-position: 0 -108px;
}

#rhfShovelerWrapper .auiTestWrapper .auiTestSprite.s_shvlNext {
     width: 36px;
     height: 39px;
     background-position: -54px 0;
}

#rhfShovelerWrapper .auiTestWrapper .auiTestSprite.s_shvlNext:hover {
     background-position: -54px -54px;
}

#rhfShovelerWrapper .auiTestWrapper .depressed .auiTestSprite.s_shvlNext {
     background-position: -54px -108px;
}

.rhfWrapper .shoveler .shoveler-heading {
    padding-right: 24em;
}


.ybh-not-signed-in-wrapper {
    width: 100%;
    margin: 11px 0 14px 20px;
}


.rhfWrapper .shoveler .shoveler-pagination {
    color: #666;
    padding: 0;
    position: absolute;
    right: 0;
    top: 0;
    width:14em;
    text-align:right;
    margin-top: -10px;
}

#rhf_container #yourBrowsingHistoryOnText {
    display: table-cell;
    float: left;
    margin-top: 19px;
    margin-left: 15px;
    margin-right: 20px;
}

#rhf_container #rhf-ybh-turn-on-link {
    display: table-cell;
    padding-top: 18px;
    float: right;
}

.ybh-not-signed-in-wrapper .ybh-turn-on-wrapper {
    display: table-cell;
    padding-top: 30px;
    float: left;
}

.ybh-not-signed-in-wrapper .rhf-sign-in-button {
    display: table-cell;
    float: right;
    padding-right: 20px;
}

.rhfWrapper .history-content {
    height: 78px;
    width: 95%;
    padding-top: 7px;
    margin: -14px 0 0px 15px;
}

.rhfWrapper .history-text {
    width: 150px;
    display: table-cell;
    white-space: nowrap;
}

.rhfWrapper #rhfViewHistoryWrapper {
    display:table;
    width: 95px;
    white-space: normal;
    overflow: hidden;
    vertical-align: top;
}

.rhfWrapper #white-mask {
    position: absolute;
    margin-top:-18px;
    background: white;
    height :18px;
    width: 90%;
}

.rhfWrapper .rhfHistoryWrapper {
    margin: 0 auto;
    width: 100%;
    min-height: 45px;
    overflow: hidden;
    display: table-cell;
}

.rhfWrapper #youViewed {
    margin-right: 3px;
    width: 45px;        /* this value is overridden in some locales */
}

.rhfWrapper #rvisColumn {
    vertical-align: top;
    height: 61px;
}

.rhf-sign-in-box {
    margin-left: 26px;
}

.rhfWrapper .shoveler #rhfUpsellColumnTitle {
    color: #666666;
    font-size: 13px;
    font-family: Arial;
    white-space: nowrap;
    float: left;
    display: block;
    margin-top: -10px;
}

.rhfWrapper #rhfUpsellColumnTitle .upsell_title_pre {
    display: inline-table;
    font-weight: bold;
}

.rhfWrapper #rhfUpsellColumnTitle .upsell_title_post {
    display: inline-table;
    white-space: normal;
    font-size: 15px;
}

.rhfWrapper #rhfUpsellColumnTitle .rvi_title {
    white-space: normal;
}

.rhfWrapper .shoveler-button-wrapper {
    width:100%;
    min-height: 310px;
    margin-bottom: -40px;
    margin-top: 10px;
}

.rhfWrapper #YBH_RVI {
    text-align:left;
    float: right;
    padding-top: 9px;
    margin-right: 14px;
    margin-bottom: 35px;
    line-height: 11px;
}

.ybh-not-signed-in-wrapper .ybh-turn-on-wrapper .youViewedText {
    padding-right: 24px !important;
}

.rhfWrapper .rvisRowWrapper {
    display: table;
}

.rhfWrapper .rvisRowWrapper .rhf-sign-in-button {
    display: table-cell;
    float: right;
}

#rhf_container .youViewedText {
    padding-top: 12px;
    padding-right: 12px;
    margin-bottom: 10px;
    line-height: 13px;
    float: left;
    border-right: 1px solid #ddd;
}

#rhf_container #rvisColumn .youViewedText {
   width: 45px;
}


.rhfWrapper #rhf_content_table {
    width: 100% !important;
    table-layout: fixed;
}

#rhf a {
    text-decoration: none;
    color: #004B91;
}

#rhf a:hover {
    color: #E47911;
}

.rhfWrapper .shoveler .start-over {
    font-size: 11px;
    font-family: Verdana;
    color: #666666;
}

.rhfWrapper .shoveler {
    position: relative;
    width: 100%;
}

.rhfWrapper .shoveler .shoveler-content {
    padding-top: 10px;
    margin: 0 35px 0 45px;
    clear:both;
}

* html .rhfWrapper .shoveler .rhfHistoryWrapper ul li {
    display: inline;
}

#rhfContainer .youViewedText p, #youViewedText p {
    margin: 0 0 1.25em;
    line-height: 13px;
}

#youViewedTextYBH {
    line-height: 13px;
    float: left;
    margin-left: 20px;
}

.rhf_container .youViewedText p, #youViewedText p, .rhf-sign-in-title {
    font-family: Arial;
    font-size: 13px;
    color: black;
}

.rhfWrapper td {
    padding: 0;
}

.rhf-sign-in-tooltip-new-customer {
    font-family: Arial;
    font-size: 11px;
}

.rhfWrapper .history-content ul {
    list-style: none;
    padding: 0;
    margin: 0;
    overflow: hidden;
    outline: none;
}

.rhfWrapper #rhf_view_history_span {
    display: table-cell;
    padding-right: 11px;
    color: rgb(204, 153, 0);
    font-weight: bold;
    font-size: 11px;
    margin-top: -3px;
}

.rhfWrapper #YBH_RVI p {
    display: table-cell;
    font-size: 10px;
    line-height: 11px;
    font-family: Arial;
}

.rhfWrapper .shoveler li p {
    text-align: left;
}

.rhfWrapper .shoveler .reason-text {
    margin-top: 3px;
}

.rhfWrapper .shoveler ul li.shoveler-progress {
    background: no-repeat center 45px url('http://g-ecx.images-amazon.com/images/G/31/x-locale/personalization/shoveler/loading-indicator._V138360146_.gif');
}

#rhf .rhfWrapper .product-link-wrapper a:hover,
#rhf .rhfWrapper .product-link-wrapper a:active {
    text-decoration: none;
    cursor: hand;
}
#rhf .rhfWrapper a:hover .title,
#rhf .rhfWrapper a:active .title {
    text-decoration: underline;
}

.rhfWrapper .title {
    font-family: arial, verdana, sans-serif;
    font-size: 13px;
    line-height: 18px;
    margin-top: 0;
}

.rhfWrapper .new-release {
    color: #009B01;
    font-weight: bold;
    font-family: verdana, arial, helvetica, sans-serif;
    font-size: 11px;
}

.rhfWrapper .byline {
    font-size: 11px;
}

.rhf-sign-in-button {
    border-left: 1px solid #ddd;
    white-space: nowrap;
    margin-top: 19px;
}

.rhf-sign-in-button .action-button, .rhf-sign-in-button a.action-button:hover,
.rhf-sign-in-button a.action-button:link, .rhf-sign-in-button a.action-button:active {
    max-width: 230px;
    text-decoration: none;
    margin-bottom: 5px;
    margin-top: 5px;
    width: 230px;
    display:block;
    background-position: -10px -170px;
    background-image: url("http://g-ecx.images-amazon.com/images/G/31/gno/beacon/BeaconSprite-IN-01._V147913113_.png");
}


.rhf-sign-in-button .action-button .action-inner,
a.action-button:link .action-inner,
a.action-button:active .action-inner,
a.action-button:hover .action-inner,
a.action-button:visited .action-inner {
    cursor: pointer;
    background-position: right -170px;
    display: block;
    height: 28px;
    position: relative;
    color: black;
    font-size: 12px;
    line-height: 28px;
    text-align: center;
    font-family: "arial","sans-serif";
    font-weight: bold;
    text-decoration: none;
    text-shadow: 0px 1px 0px #ffe093;
}

.rhfWrapper #rhf_nav_back {
    margin: 15px 30px 30px 30px;
    font-size: 13px;
    font-style: italic;
    float: left;
}

.rhfWrapper .rhf-divider-inner {
    height: 23px;
    margin-bottom: -6px;
    background: -moz-linear-gradient(top,#ddd,#f7f7f7 3px,white);
    background: -webkit-gradient(linear,left top,left bottom,color-stop(0%,#ddd),color-stop(3px,#f7f7f7),color-stop(100%,white));
    background: -webkit-linear-gradient(top,#ddd,#f7f7f7 3px,white);
    background: -o-linear-gradient(top,#ddd,#f7f7f7 3px,white);
    background: -ms-linear-gradient(top,#ddd,#f7f7f7 3px,white);
    background: linear-gradient(top,#ddd,#f7f7f7 3px,white);
    filter: none;
    z-index: 0;
    zoom: 1;
}

.rhfWrapper .rhf-divider-inner:after {
    display: block;
    width: 100%;
    height: 44px;
    background-color: transparent;
    background: -moz-linear-gradient(left,white,rgba(255,255,255,0),white);
    background: -webkit-gradient(linear,left top,right top,color-stop(0%,white),color-stop(50%,rgba(255,255,255,0)),color-stop(100%,white));
    background: -webkit-linear-gradient(left,white,rgba(255,255,255,0),white);
    background: -o-linear-gradient(left,white,rgba(255,255,255,0),white);
    background: -ms-linear-gradient(left,white,rgba(255,255,255,0),white);
    background: linear-gradient(left,white,rgba(255,255,255,0),white);
    filter: none;
    z-index: 1;
    content: "";
}

#rhf_container #yourBrowsingHistoryOnText p {
    font-size: 13px;
    color: #ddd;
    font-style: italic;
}

.rhfWrapper .rhf-RVIs a img {
    border-style: solid;
    border-width: 1px;
    border-color: #ddd;
    box-sizing: border-box;
    -moz-box-sizing: border-box; /* FireFox */
    -webkit-box-sizing: border-box; /* Safari */
}

.rhfWrapper .rhf-RVIs a:hover img {
    border: 2px solid #E47911;
}

.rhfWrapper .arrowImg {
    position: absolute;
    margin-top: 2px;
    visibility: hidden;
}

.rhfWrapper #youViewed #youViewedText {
    margin-bottom: -13px;
    padding-top: 12px;
}

.rhfWrapper #rhf-recs-down-text {
    padding-top: 13px;
    font-size: 16px;
    line-height: 26px;
}

.rhfWrapper .rhfHistoryWrapper li {
    float: left;
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 3px;
    list-style-type: none;
}

.rhfWrapper .rhfHistoryWrapper .byline {
    color: #666666;
}

.rhfWrapper .rating {
    margin-top: 2px;
}

.rhfWrapper .binding {
    color: #666666;
    font-size: 11px;
}

.rhfWrapper .shoveler .binding {
    margin-top: 2px;
}

.rhfWrapper .shoveler .price {
    margin-top: 2px;
    color: #900;
    font-size: 13px;
}

.rhfWrapper .shoveler .price .price-suffix {
    color: #666666;
}
.rhfWrapper .shoveler .price-label {
    color: #888888;
    font-size: 12px;
    font-family: Arial, sans-serif;
    letter-spacing: normal;
}

.rhfWrapper .shoveler .price .unit {
    color: #666;
    font-size: 12px;
}

.rhfWrapper .shoveler .priceText { font-size: 12px };
.rhfWrapper .shoveler .price-per-unit {
    font-size:10px;
    color:#990000;
    margin-left:.25em;
    white-space:nowrap;
}

.rhfWrapper .shoveler .primeExplanation {
    color: #666666;
    font-size: 11px;
}

.rhfWrapper .RobinBadgeSmall {
    background-position: -9px -17px;
    background-repeat: no-repeat;
    background-size: 125px 50px;
    display: inline-block;
    height: 14px;
    width: 47px;
}

.rhfWrapper #rhfNoRecsMessage {
    color: #666666;
    font-size: 13px;
    font-family: Arial;
}

.rhfWrapper .rhfHistoryWrapper #rhfHistoryColumnTitle {
    color: #666666;
    font-size: 13px;
    font-family: Arial;
}

.rhfWrapper .popoverTrigger {
    margin-left:.35em;
    cursor:default;
}

.rhfWrapper #rhfShovelerWrapper{
    display: block;
    height: 310px;
}

.rhfWrapper #rhfDividerColumn {
    border-top: 1px solid #ddd;
}
* html .rhf {
    height:1%;
}

.rhfWrapper #rhfUpsellColumnWrapper {
    padding: 10px 10px 0 10px;
}
.rhfWrapper .shoveler div.disabled-button {
    opacity: 0.2;
    -moz-opacity: 0.2;
    filter: alpha(opacity=20);
    cursor: default;
}
.rhfWrapper .shoveler .disclaim {
    margin-bottom: 15px;
}

#rhf_container .carat {
    font-size: 11px;
    color: #E47911;
    line-height: 0;
    margin: 0 3px 0 0;
    font-weight: bold;
}

.rhfWrapper .shoveler ul {
    height: 300px !important;
    padding: 0;
    margin: 0;
    overflow:hidden;
    outline: none;
    font-size: 86%;
}

.rhfWrapper .shoveler ul li {
    float: left;
    margin: 0;
    padding: 0;
    width: 155px;
    height: 300px !important;
    overflow: hidden;
}

#rhf_footer {
    padding: 10px;
    text-align: left;
    font-size: 13px;
}
.price {
    color: #990000;
}

.price-suffix {
    color: #666666;
}
.primeExplanation {
    font-size: 11px;
}
.a-carousel-slide .a-carousel {
    transform-style: flat;
}
.a-carousel-card {
    white-space: normal;
}




</style>
    <br />
    <div id="rhf" class="copilot-secure-display" style="clear:both">


    <table id="rhf_table" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td class="rhf-box-corner-sprite rhf-box-tl" width="15"></td>
            <td class="rhf-box-corner-sprite rhf-box-tc">
            <div class="rhf_header"><span id="rhfMainHeading">Your Recently Viewed Items and Featured Recommendations</span>&nbsp;</div>
            </td>
            <td class="rhf-box-corner-sprite rhf-box-tr" width="15"></td>
        </tr>
        <tr>
            <td class="rhf-box-sides-sprite rhf-box-l" width="15">&nbsp;</td>
	    <td>
            <div id="rhf_container" style="display:none;">





<div class='rhf_loading_outer'><table class='rhf_loading_middle'><tr><td class='rhf_loading_inner'><img src='http://g-ecx.images-amazon.com/images/G/31/ui/loadIndicators/loadIndicator-large._V138348995_.gif' /></td></tr></table></div>


<script type="text/JavaScript">

window.rhf_use_AUI = 1 && typeof P === 'object' && P.AUI_BUILD_DATE;


window.rhf_use_AUI_lib = typeof P === 'object' && P.AUI_BUILD_DATE;

if (!window.rhf_use_AUI_lib) {


amznJQ.addLogical('p13nlogger', ['http://z-ecx.images-amazon.com/images/G/01/browser-scripts/p13nlogger/p13nlogger-3861958816._V1_.js']);
amznJQ.addLogical('callOnVisible', ['http://z-ecx.images-amazon.com/images/G/01/browser-scripts/callOnVisible/callOnVisible-66186444._V1_.js']);

var rhfP13NLogger = function(rhfWaitTime, success) {
    amznJQ.onReady('callOnVisible', function () {
        var rhfContainer = jQuery("#rhf_container");
        var action = success ? 'view' : 'ajax_failure';
       	if (typeof rhfContainer.callOnVisible == 'function') {
	    rhfContainer.callOnVisible(function () {
                var rhfLog = function(eventData) {
		    amznJQ.onReady('p13nlogger', function() {
			var commonData = {
		            channel: 'recommendations',
			    widget: 'pd_rhf',
			    featureElement: rhfContainer,
			    requestInfoElement: '#rhf0RequestInfo'
			};
			p13n.logEvent(jQuery.extend({}, commonData, eventData));
		    });
		};
		rhfLog({
		   action: action,
		   page: 1,
		   eventtime: rhfWaitTime,
		   meta: {'isRHFLoaded': success}
		});
	    }, 0);
        }
    });
};

var rhfRVIP13NLogger = function() {
        var rviContainer = jQuery("#horizontal-list");
        var shvlContainer = jQuery('#rhf_upsell_div');
        var isEventComplete = function() {
            return shvlContainer.find('.rhf_loading_outer').size() == 0;
        };
        var rviLog = function(eventData) {
            amznJQ.onReady('p13nlogger', function() {
               var commonData = {
                   channel: 'recommendations',
                   widget: 'pd_rhf',
                   isEventComplete: isEventComplete,
                   featureElement: shvlContainer,
                   requestInfoElement: '#rhf0RequestInfo'
               };
              p13n.logAsyncEvent(jQuery.extend({}, commonData, eventData));
            });
        };
        rviContainer.find('.rhf-RVIs').click(function() {
            rviLog({
                action: 'rvi_click',
                page: 1
            });
        });
        rviContainer.find('.clearSelection').click(function() {
            rviLog({
                action: 'clear_click',
                page: 1
            });
        });
};

}

var rhfShovelerBootstrapFunction = function($) { (function($) {

    window.RECS_rhfShvlLoading = false;
    window.RECS_rhfShvlLoaded = false;
    window.RECS_rhfInView = false;
    window.RECS_rhfMetrics = {};

    var rhfWaitTime = 0;

    $("#rhf_container").show();
    var rhfShvlEventHandler = function () {
        if (   ! window.RECS_rhfShvlLoaded
            && ! window.RECS_rhfShvlLoading
            && $('#rhf_container').size() > 0 ) {
            var yPosition = $(window).scrollTop() + $(window).height();
            var rhfElementFound = $('#rhfMainHeading').size();
            var rhfPosition = $('#rhfMainHeading').offset().top;

            if (/webkit.*mobile/i.test(navigator.userAgent)) {
                rhfPosition -= $(window).scrollTop();
            }

            if (rhfElementFound && ( rhfPosition - yPosition < 400 )) {
                window.RECS_rhfMetrics["start"] = (new Date()).getTime();
                window.RECS_rhfShvlLoading = true;
                var handleSuccess = function (html) {
                    $("#rhf_container").html(html);
                    $("#rhf0Shvl").trigger("render-shoveler");
                    window.RECS_rhfShvlLoaded = true;
                    window.RECS_rhfMetrics["loaded"] = (new Date()).getTime();
                    if (!window.rhf_use_AUI_lib) {
                        rhfWaitTime = window.RECS_rhfMetrics["loaded"] - window.RECS_rhfMetrics["inView"];
                        rhfP13NLogger(rhfWaitTime, true);
                        rhfRVIP13NLogger();
                    }
                    //If RHF is loaded, remove the interval.
                    if ("C" === "T1" && window.rhf_trigger_event) {
                        clearInterval(window.rhf_trigger_event);
                    }
                };
                var handleError = function () {
                    $("#rhf_container").hide();
                    $("#rhf_error").show();
                    window.RECS_rhfMetrics["loaded"] = "error";
                    if (!window.rhf_use_AUI_lib) {
                        rhfP13NLogger(rhfWaitTime, false);
                    }
                    //If RHF fails to load, remove the interval.
                    if ("C" === "T1" && window.rhf_trigger_event) {
                        clearInterval(window.rhf_trigger_event);
                    }
                };
                var ajaxURL = '/gp/history/external/full-rhf-rec-handler.html';
                var ajaxArgs = {
                    type: "POST",
                    timeout: 10000,
                    data: {
                        rhfAsins        : '',
                        shovelerName    : 'rhf0',
                        key             : 'rhf',
                        numToPreload    : '8',
                        isGateway       : 0,
                        refTag          : 'pd_rhf_se',
                        parentSession   : '277-2541869-5922526',
                        relatedRequestId: '0X849WPJZKXMCE756NPF',
                        excludeASIN     : '',
                        renderPopover   : 0,
                        forceSprites    : 0,
                        currentPageType : 'Search',
                        currentSubPageType : 'portal-batch-slow-btf',
                        weblabTriggers  : "",
                        // We'll pretend that AUI is disabled everywhere until all AUI carousel bugs are fixed.
                        isAUI           : window.rhf_use_AUI ? 1 : 0
                    },
                    dataType: "json",
                    success: function (data, status) {
                        if (typeof(data) === 'object' && data.success && data.html) {
                            handleSuccess(data.html);
                            if (window.rhf_use_AUI) {
                                P.when("jQuery", "a-carousel-framework").execute(function(jQuery, framework){
                                  jQuery("#rhf_upsell_div .a-carousel-viewport").addClass("a-carousel-slide");
                                  framework.createAll();
                                });
                            }
                        } else {
                            handleError();
                        }
                    },
                    error: function (xhr, status) {
                        handleError();
                    }
                };
                if (window.rhf_use_AUI) {
                    P.when("A").execute(function (A) {
                        A.$.ajax(ajaxURL, ajaxArgs);
                    });
                } else {
                    ajaxArgs['url'] = ajaxURL;
                    $.ajax(ajaxArgs);
                }
            }
        }
    };
    var getDuplicateASINList = function() {
        var cartRecsASINList;
        if (window.rhf_use_AUI) {
            var cartCarouselParams = $("div[data-p13n-widget = 'pd_cart_recs']").attr("data-a-carousel-options");
            if (cartCarouselParams) {
                cartRecsASINList = JSON.parse(cartCarouselParams).ajax.id_list;
                //Get first 10 of the List, will get all of them if less than 10
                return JSON.stringify(cartRecsASINList.slice(0, 10));
            }
        } else if (window.RECS_cartRecs_ASINList) {
            cartRecsASINList = window.RECS_cartRecs_ASINList;
            return JSON.stringify(cartRecsASINList.slice(0, 10));
        }
        return cartRecsASINList;
    };
    var rhfInView = function() {
        if (!window.RECS_rhfInView && $('#rhf_container').size() > 0) {
            var yPosition = $(window).scrollTop() + $(window).height();
            var rhfElementFound = ($('#rhfMainHeading').size() > 0);
            var rhfPosition = $('#rhfMainHeading').offset().top;
            if (/webkit.*mobile/i.test(navigator.userAgent)) {
                rhfPosition -= $(window).scrollTop();
            }
            if (rhfElementFound && ( rhfPosition - yPosition < 0 )) {
                window.RECS_rhfInView = true;
                window.RECS_rhfMetrics["inView"] = (new Date()).getTime();
                if ("C" === "T1" && window.rhf_inView_event) {
                    clearInterval(window.rhf_inView_event);
                }
            }
        }
    };
    window.rhfYBHTurnOn = function () {
            $.ajax({
                  url: '/gp/history/external/full-rhf-ybh-on-handler.html',
                  type: "POST",
                  timeout: 2000,
                  data: {
                         parentSession    : '277-2541869-5922526'
                  },
                  dataType: "text",
                  success: function (data, status) {
                               $("#yourBrowsingHistoryOnText").find('p').html("You don't have any recently viewed Items.");
                               $("#rhf-ybh-turn-on-link").hide();
                  }
            });
    };
    $(document).ready(rhfShvlEventHandler);
    $(document).ready(rhfInView);

    if ("C" === "T1") {
        //We met some problems with jQuery scroll function, so we decide to use setInterval for checking RHF triggering status.
        //https://tt.amazon.com/0026187346
        window.rhf_trigger_event = setInterval(function () {
            if (!window.RECS_rhfShvlLoaded
                && !window.RECS_rhfShvlLoading
                && $('#rhf_container').size() > 0) {
                rhfShvlEventHandler();
            }
        }, 200);

        window.rhf_inView_event = setInterval(function () {
            if ( !window.RECS_rhfInView && $('#rhf_container').size() > 0) {
                rhfInView();
            }
        }, 200);
    } else {
        $(window).scroll(rhfShvlEventHandler);
        $(window).scroll(rhfInView);
    }

})($); }
if (window.rhf_use_AUI) {
    //Register a component
    P.when('jQuery', 'ready').register('rhf-bootstrapper', function($){
       return {
            bootstrap : function(){
                return rhfShovelerBootstrapFunction($);
            }
       };
    });
    //Use that component after it initializes
    P.when('rhf-bootstrapper').execute(function(rhfBootstrapper){
        rhfBootstrapper.bootstrap();
    });
} else {
    amznJQ.onReady(
        'jQuery',
        function () {
            rhfShovelerBootstrapFunction(jQuery);
        }
     );
}
</script>

</div><noscript>






<table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top: 10px">
    <tr valign="top">
        <td valign="top">
            <div class="rhfHistoryWrapper">
                <p>After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.</p>
            </div>
        </td>
    </tr>
    <tr><td>
    <div style="padding:10px 10px 0 10px; text-align:left;">
        <b><span style="color: rgb(204, 153, 0); font-weight: bold; font-size: 13px;"> &#8250; </span>
        <a href="/gp/yourstore/pym/ref=pd_pyml_rhf">View and Edit Your Browsing History</a>
        </b></div>
    </td></tr>
</table>
</noscript><div id="rhf_error" style="display:none;">






<table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-top: 10px">
    <tr valign="top">
        <td valign="top">
            <div class="rhfHistoryWrapper">
                <p>After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.</p>
            </div>
        </td>
    </tr>
    <tr><td>
    <div style="padding:10px 10px 0 10px; text-align:left;">
        <b><span style="color: rgb(204, 153, 0); font-weight: bold; font-size: 13px;"> &#8250; </span>
        <a href="/gp/yourstore/pym/ref=pd_pyml_rhf">View and Edit Your Browsing History</a>
        </b></div>
    </td></tr>
</table>
</div><div id="rhf_recs_error" style="display:none;">




<div id="rhf-recs-service-down" align="center" style="padding-top: 24px;">
    <div id="rhf-recs-down-text">
        <p>Our recommendations service is currently unavailable. Please refresh this page or try again later.</p>
        <p>We apologize for the inconvenience!</p>
    </div>
</div>
</div>
            </td>
            <td class="rhf-box-sides-sprite rhf-box-r" width="15"></td>
        </tr>
    </table>
    </div>
    <br />

</div><!-- footer pilu -->



















<div id="navFooter"><table class="navFooterVerticalColumn" cellspacing="0" align="center"><tr><td class="navFooterLinkCol"><div class="navFooterColHead">Get to Know Us</div><ul><li class="nav_first"><a href="/b/ref=gw_m_b_corporate?ie=UTF8&amp;node=1592138031" class="nav_a">About Us</a></li><li><a href="http://amazon.jobs" class="nav_a">Careers</a></li><li><a href="/b/ref=footer_press?ie=UTF8&amp;node=1592137031" class="nav_a">Press Releases</a></li><li class="nav_last"><a href="/Online-Charity/b/ref=footer_cares?ie=UTF8&amp;node=4594605031" class="nav_a">Gift a Smile</a></li></ul></td><td class="navFooterColSpacerInner"></td><td class="navFooterLinkCol"><div class="navFooterColHead">Connect with Us</div><ul><li class="nav_first"><a href="http://www.amazon.in/gp/redirect.html/ref=footer_fb?location=http://www.facebook.com/AmazonIN&amp;token=6BD0FB927CC51E76FF446584B1040F70EA7E88E1" class="nav_a">Facebook</a></li><li><a href="http://www.amazon.in/gp/redirect.html/ref=footer_twitter?location=http://twitter.com/AmazonIN&amp;token=7A1A4AE8F6CE0BD277D8295E58702D283F329C0F" class="nav_a">Twitter</a></li><li class="nav_last"><a href="https://www.amazon.in/gp/redirect.html/ref=footer_blog?_encoding=UTF8&amp;location=http://blog.amazon.in" class="nav_a">The Amazon.in Blog</a></li></ul></td><td class="navFooterColSpacerInner"></td><td class="navFooterLinkCol"><div class="navFooterColHead">Make Money with Us</div><ul><li class="nav_first"><a href="https://www.amazon.in/refer-and-earn" class="nav_a">Refer & Earn Rs.200</a></li><li><a href="http://services.amazon.in/services/sell-on-amazon/benefits.html/ref=az_footer_soa?ld=AWRGINSOAfooter" class="nav_a">Sell on Amazon</a></li><li><a href="https://www.amazon.in:443/gp/redirect.html/ref=footer_assoc?_encoding=UTF8&amp;location=https%3A%2F%2Faffiliate-program.amazon.in%2F%3Futm_campaign%3Dassocshowcase%26utm_medium%3Dfooter%26utm_source%3DGW&amp;source=standards&amp;token=680FE811DE27E32BF3D5179FEDA69BDF16FC904C" class="nav_a">Become an Affiliate</a></li><li class="nav_last"><a href="http://services.amazon.in/services/fulfilment-by-amazon/benefits.html/ref=az_footer_fba?ld=AWRGINFBAfooter" class="nav_a">Fulfilment by Amazon</a></li></ul></td><td class="navFooterColSpacerInner"></td><td class="navFooterLinkCol"><div class="navFooterColHead">Let Us Help You</div><ul><li class="nav_first"><a href="/gp/css/homepage.html/ref=footer_ya" class="nav_a">Your Account</a></li><li><a href="/gp/help/customer/display.html/ref=footer_shiprates?ie=UTF8&amp;nodeId=200534000" class="nav_a">Delivery Speeds & Charges</a></li><li><a href="/gp/css/returns/homepage.html/ref=hy_f_4" class="nav_a">Returns Centre</a></li><li><a href="/gp/help/customer/display.html/ref=footer_swc?ie=UTF8&amp;nodeId=201083470" class="nav_a">100% Purchase Protection</a></li><li class="nav_last"><a href="/gp/help/customer/display.html/ref=gw_m_b_he?ie=UTF8&amp;nodeId=200507590" class="nav_a">Help</a></li></ul></td></tr></table>

<div class="navFooterLine navFooterLogoLine"><a href="/ref=footer_logo"><img src="http://g-ecx.images-amazon.com/images/G/31/gno/images/general/navAmazonLogoFooter._V391206769_.gif" width="98" alt="amazon.in" height="28" border="0" /></a></div>

<div class="navFooterLine navFooterLinkLine navFooterPadItemLine"><ul><li class="nav_first"><a href="http://www.amazon.com.au" class="nav_a">Australia</a></li><li><a href="http://www.amazon.com.br" class="nav_a">Brazil</a></li><li><a href="http://www.amazon.ca" class="nav_a">Canada</a></li><li><a href="http://www.amazon.cn" class="nav_a">China</a></li><li><a href="http://www.amazon.fr" class="nav_a">France</a></li><li><a href="http://www.amazon.de" class="nav_a">Germany</a></li><li><a href="http://www.amazon.it" class="nav_a">Italy</a></li><li><a href="http://www.amazon.co.jp" class="nav_a">Japan</a></li><li><a href="http://www.amazon.com.mx/" class="nav_a">Mexico</a></li><li><a href="http://www.amazon.nl/" class="nav_a">Netherlands</a></li><li><a href="http://www.amazon.es" class="nav_a">Spain</a></li><li><a href="http://www.amazon.co.uk" class="nav_a">United Kingdom</a></li><li class="nav_last"><a href="http://www.amazon.com" class="nav_a">United States</a></li></ul></div>

<div class="navFooterLine navFooterLinkLine navFooterDescLine"><table cellspacing="0"><tr>
<td class="navFooterDescSpacer" style="width: 40.0%"></td>
<td class="navFooterDescItem"><a href="http://www.abebooks.com/" class="nav_a">AbeBooks<br/> <span class="navFooterDescText">Rare Books<br/> & Textbooks</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://aws.amazon.com/what-is-cloud-computing/?sc_channel=EL&amp;sc_campaign=IN_amazonfooter" class="nav_a">Amazon Web Services<br/> <span class="navFooterDescText">Scalable Cloud<br/> Computing Services</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.audible.com/" class="nav_a">Audible<br/> <span class="navFooterDescText">Download<br/> Audio Books</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.diapers.com/" class="nav_a">Diapers.com<br/> <span class="navFooterDescText">Everything<br/> But The Baby</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.dpreview.in/" class="nav_a">DPReview<br/> <span class="navFooterDescText">Digital<br/> Photography</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.imdb.in/" class="nav_a">IMDb<br/> <span class="navFooterDescText">Movies, TV<br/> & Celebrities</span></a></td>
<td class="navFooterDescSpacer" style="width: 40.0%"></td>
</tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescSpacer" style="width: 40.0%"></td>
<td class="navFooterDescItem"><a href="http://www.junglee.com/" class="nav_a">Junglee.com<br/> <span class="navFooterDescText">Shop Online<br/> in India</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.look.com/" class="nav_a">Look.com<br/> <span class="navFooterDescText">Kids' Clothing<br/> & Shoes</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.myhabit.com/" class="nav_a">MYHABIT<br/> <span class="navFooterDescText">Private Fashion<br/> Designer Sales</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.shopbop.com/" class="nav_a">Shopbop<br/> <span class="navFooterDescText">Designer<br/> Fashion Brands</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.yoyo.com/" class="nav_a">Yoyo.com<br/> <span class="navFooterDescText">A Happy Place<br/> To Shop For Toys</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 40.0%"></td>
</tr>
</table></div>

<div class="navFooterLine navFooterLinkLine navFooterPadItemLine"><ul><li class="nav_first"><a href="/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&amp;nodeId=200545940" class="nav_a">Conditions of Use & Sale</a></li><li class="nav_last"><a href="/gp/help/customer/display.html/ref=footer_privacy?ie=UTF8&amp;nodeId=200534380" class="nav_a">Privacy Notice</a></li></ul><span>© 1996-2015, Amazon.com, Inc. or its affiliates</span><ul></ul></div>
</div>

<!-- whfh-UY3HNjt0yw8LNf9ecABPOKa5ZWHpmpdG5YpA19L+utV42pejlfUQ7w== rid-0X849WPJZKXMCE756NPF -->











<div id="sis_pixel_r2" aria-hidden="true" style="height:1px;"></div><script>(function(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.addEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=document.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="//aax-eu.amazon-adsystem.com/s/iu3?d=amazon.in&slot=navFooter&a2=010184ad38be6cec32d3cbb7cfbf9e7d750ed71d8e688624ea5bb80b04f8a1c76ab0&old_oo=0&cb=1431746869267" width="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>')},300)});</script><!-- footer tilu -->


<script>
amzn.sx.utils.jsDepMgr.when("jQuery", "addBottomJS", function(jQuery) {
  var $ = jQuery;


amzn.sx.utils.jsDepMgr.when("cp", "addBottomJSCP", function() {
  if($.cp) {
    $.cp.init({
      algo: 0,
      verbose: 0,
      waitTime: 500
    });
  }
});
});
</script>
</div>

        <div id='be' style="display:none;visibility:hidden;"><form name='ue_backdetect' action="get"><input type="hidden" name='ue_back' value='1' /></form>

    <script type="text/javascript">
(function(d){d._uess=function(){var a="";screen&&screen.width&&screen.height&&(a+="&sw="+screen.width+"&sh="+screen.height);var b=function(a){var b=document.documentElement["client"+a];return"CSS1Compat"===document.compatMode&&b||document.body["client"+a]||b},c=b("Width"),b=b("Height");c&&b&&(a+="&vw="+c+"&vh="+b);return a}})(ue_csm);

(function(a){var b=document.ue_backdetect;b&&b.ue_back&&a.ue&&(a.ue.bfini=b.ue_back.value);a.uet&&a.uet("be");a.onLdEnd&&(window.addEventListener?window.addEventListener("load",a.onLdEnd,!1):window.attachEvent&&window.attachEvent("onload",a.onLdEnd));a.ueh&&a.ueh(0,window,"load",a.onLd,1);a.ue&&a.ue.tag&&(a.ue_furl&&a.ue_furl.split?(b=a.ue_furl.split("."))&&b[0]&&a.ue.tag(b[0]):a.ue.tag("nofls"))})(ue_csm);

(function(b){b._uec=function(b){var a=window.performance;if(0===(a?a.navigation.type:0)){var a="; expires="+(new Date(+new Date+6048E5)).toGMTString(),c=+new Date-ue_t0;if(0<c){var d="|"+ +new Date;document.cookie="csm-hit="+(b/c).toFixed(2)+d+a+"; path=/"}}}})(ue_csm);


(function(b,c){var a=c.images;a&&a.length&&b.ue.count("totalImages",a.length)})(ue_csm,document);


(function(g,e){function h(a){a=a.split("?")[0]||a;a=a.replace("http://","").replace("https://","").replace("resource://","").replace("res://","").replace("undefined://","").replace("chrome://","").replace(/\*/g,"").replace(/!/g,"").replace(/~/g,"");var b=a.split("/");a=a.substr(a.lastIndexOf("/")+1);b.splice(-1);b=b.map(function(a){c[a]||(c[a]=(k++).toString(36));return c[a]});b.push(a);return b.join("!")}function l(){return e.getEntriesByType("resource").filter(function(a){return d._rre(a)<d._ld}).sort(function(a,
b){return a.responseEnd-b.responseEnd}).splice(0,m).map(function(a){var b=[],c;for(c in a)f[c]&&a[c]&&b.push(f[c]+Math.max(a[c]|0,-1).toString(36));b.push("i"+a.initiatorType);(1==d._rtn&&d._afjs>n||2==d._rtn)&&b.push("n"+h(a.name));return b.join("_")}).join("*")}function p(){var a="pm",b;for(b in c)c.hasOwnProperty(b)&&(a+="*"+c[b]+"_"+b);return a}function q(){d.log({k:"rtiming",value:l()+"~"+p()},"csm")}if(e&&e.getEntriesByType&&Array.prototype.map&&Array.prototype.filter){var f={connectStart:"c",
connectEnd:"C",domainLookupStart:"d",domainLookupEnd:"D",duration:"z",fetchStart:"f",redirectStart:"r",redirectEnd:"R",requestStart:"q",responseStart:"s",responseEnd:"S",startTime:"a"},d=g.ue,c={},k=1,n=20,m=200;d&&d._rre&&(d._art=function(){d._ld&&window.setTimeout(q,0)})}})(ue_csm||{},window.performance);



(function(c,d){var b=c.ue,a=d.navigator;b&&b.tag&&a&&(a=a.connection||a.mozConnection||a.webkitConnection)&&a.type&&b.tag("netInfo:"+a.type)})(ue_csm,window);


var ue_pty="Search",
    ue_spty=null,
    ue_pti=null;

</script>

</div>

<noscript>
    <img height="1" width="1" style='display:none;visibility:hidden;' src='//fls-eu.amazon.com/1/batch/1/OP/A21TJRUUN4KGV:277-2541869-5922526:0X849WPJZKXMCE756NPF$uedata=s:%2Fmn%2Fsearch%2Fuedata%2F277-2541869-5922526%3Fnoscript%26id%3D0X849WPJZKXMCE756NPF:0' alt=""/>
</noscript>
</div></body></html>"""
#url = 'http://www.amazon.in/s/ref=nb_sb_noss_1/275-5930167-4161031?url=search-alias%3Daps&field-keywords=smartphones&sprefix=smartphones%2Caps'
#response = urllib.request.urlopen(url)
#data = response.read()      # a `bytes` object
#text = data.decode('utf-8')

soup=BeautifulSoup(html)
#To print in html format
#print (soup.prettify())
#print (json.dumps(soup))

#To find the product name
#productTitle=soup.find_all("")
#productTitle=soup.select(".a-size-medium a-color-null s-inline s-access-title a-text-normal")
productTitle=soup.find_all("h2", {"class" : "a-size-medium a-color-null s-inline s-access-title a-text-normal"})
for product in productTitle:
    print(product.text)

#price=soup.find_all("span", {"class" : "a-size-base a-color-price s-price a-text-bold"})
#print (price)

#To find the reviews from Amazon.in
#reviews=soup.find_all("a", {"class" : "a-size-small a-link-normal a-text-normal"})
#print (reviews)

#To find the rating from Amazon.in
#rating=soup.find_all("span", {"class" : "a-icon-alt"})
#print (rating)
reviews=soup.find_all("a", {"class" : "a-size-small a-link-normal a-text-normal"})
for review in reviews:
    print(review.text)
