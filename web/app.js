'use strict';
const $ = selector => document.querySelector(selector);
const state = {all:[],visible:[],filter:'all',query:'',page:1,pageSize:'all',user:null,wallet:null,requestId:0};
let serverAnchor = 0, wallAnchor = 0, noticeTimeout;
const names = {ord_active:'Everyday essentials',ord_before:'A little something',ord_boundary:'Desk favourites',ord_cancelled:'Weekend supplies',ord_expired:'The refill order',ord_paid:'The weekend order',ord_ben:'Everyday essentials'};
const statusNames = {draft:'Draft',pending_payment:'Awaiting payment',paid:'Payment received',fulfilling:'Preparing order',fulfilled:'Collected',cancelled:'Cancelled',refunded:'Refunded'};
const messages = {invalid_credentials:'That email and password don’t match. Please try again.',authentication_required:'Please sign in to view your account.',order_not_found:'We couldn’t find an order with that reference.',order_not_payable:'This order is no longer awaiting payment.',login_state_missing_or_invalid:'Your sign-in could not be confirmed. Please try again.',invalid_request:'Please check the request and try again.'};
const escape = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const icon = name => `<svg class="icon" aria-hidden="true"><use href="#${name}"/></svg>`;
const money = (minor,currency='NGN') => new Intl.NumberFormat('en-NG',{style:'currency',currency,minimumFractionDigits:2}).format(minor/100);
function dateTime(value) { return new Intl.DateTimeFormat('en-GB',{timeZone:'Africa/Lagos',day:'2-digit',month:'short',year:'numeric',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date(value)); }
function statusBadge(order) { return `<span class="status-pill status-${escape(order.status)}">${escape(statusNames[order.status] || order.status)}</span>`; }
function notify(text,error=false) {
  clearTimeout(noticeTimeout); $('#notice').textContent=text; $('#notice').hidden=false;
  $('#notice').classList.toggle('error',error);
  noticeTimeout=setTimeout(() => { $('#notice').hidden=true; },6500);
}
async function request(path, options={}) {
  const response=await fetch(path,options);
  const data=await response.json();
  if (!response.ok) throw new Error(data.code || 'request_failed');
  return data;
}
function showError(error) { notify(messages[error.message] || `We couldn’t complete that request (${error.message}).`,true); }
function showSignIn() { $('#login').hidden=false; $('#dashboard').hidden=true; document.title='HarbourDesk — Welcome back'; }
function showAccount() {
  $('#login').hidden=true; $('#dashboard').hidden=false;
  $('#account-name').textContent=state.user.name;
  $('#account-email').textContent=state.user.email;
  $('#avatar').textContent=state.user.name.slice(0,1);
}
function syncClock(value) {
  serverAnchor=Date.parse(value); wallAnchor=Date.now();
  $('#clock').textContent=`As of ${dateTime(value)} WAT`;
  $('#clock').title=value;
}
function updateSummary() {
  $('#pending-count').textContent=state.all.filter(o=>o.status==='pending_payment').length;
  $('#paid-count').textContent=state.all.filter(o=>o.status==='paid').length;
  $('#nav-order-count').textContent=state.all.length;
  $('#order-total').textContent=state.all.length;
}
async function loadOrders() {
  const current=++state.requestId;
  try {
    const data=await request('/api/orders');
    let visible=data.orders;
    const paged=state.pageSize!=='all' && state.query==='' && state.filter==='all';
    if (state.query!=='') {
      // Preserve the typed query: the search exercise investigates normalization on the server.
      visible=(await request(`/api/search?q=${encodeURIComponent(state.query)}`)).orders;
    } else if (paged) {
      // Use one-based API pages directly; do not mask the starter's pagination defect in the UI.
      visible=(await request(`/api/orders?page=${state.page}&page_size=${state.pageSize}`)).orders;
    }
    if (current!==state.requestId) return;
    state.all=data.orders;
    state.visible=state.filter==='all' ? visible : visible.filter(o=>o.status===state.filter);
    syncClock(data.server_now); updateSummary(); renderOrders(paged);
  } catch(error) { if (error.message==='authentication_required') showSignIn(); else showError(error); }
}
function renderOrders(paged) {
  $('#orders').innerHTML=state.visible.map(order=>`<article class="order-row" data-order-id="${escape(order.id)}">
    <div class="order-tile" aria-hidden="true">${icon('box')}</div>
    <div class="order-description"><strong class="order-title">${escape(names[order.id] || 'Collection reservation')}</strong><span class="order-reference">${escape(order.id)}</span><div class="order-meta">Reserved ${escape(dateTime(order.created_at))} WAT</div></div>
    <div class="order-state">${statusBadge(order)}${order.status==='pending_payment' ? `<div class="countdown" data-expires="${escape(order.expires_at)}">${icon('clock-icon')}<span></span></div>` : `<div class="countdown">${order.status==='paid' ? 'Payment recorded' : 'See order details'}</div>`}</div>
    <div class="order-amount">${escape(money(order.amount_minor,order.currency))}<small>Total amount</small></div>
    <div class="order-actions">${order.status==='pending_payment' ? `<button class="primary" data-open="${escape(order.id)}">Pay now ${icon('arrow')}</button>` : ''}<button class="text-button" data-open="${escape(order.id)}">View details ↗</button></div>
  </article>`).join('');
  $('#empty-orders').hidden=state.visible.length>0;
  $('#result-count').textContent=`${state.visible.length} ${state.visible.length===1 ? 'order' : 'orders'} shown${state.query!=='' ? ' · Search results' : ''}`;
  $('#pagination').hidden=!paged;
  $('#page-label').textContent=`Page ${state.page}`;
  $('#previous').disabled=state.page<=1;
  $('#next').disabled=state.page>=Math.max(1,Math.ceil(state.all.length/Number(state.pageSize)));
  updateCountdowns();
}
function updateCountdowns() {
  const elapsed=Date.now()-wallAnchor;
  for (const label of document.querySelectorAll('[data-expires]')) {
    const seconds=Math.max(0,Math.ceil((Date.parse(label.dataset.expires)-serverAnchor-elapsed)/1000));
    label.classList.toggle('expired',seconds===0);
    label.querySelector('span').textContent=seconds ? `Expires in ${Math.floor(seconds/60)}m ${String(seconds%60).padStart(2,'0')}s` : 'Reservation expired';
    // The intentional expiry exercise remains: eligibility currently depends on status alone.
  }
}
async function openOrder(id) {
  try {
    const order=await request(`/api/orders/${encodeURIComponent(id)}`);
    $('#order-detail').innerHTML=`<h2 id="detail-title">${escape(names[order.id] || 'Collection reservation')}</h2>${statusBadge(order)}
      <div class="detail-amount">${escape(money(order.amount_minor,order.currency))}<small>Order total · ${escape(order.currency)}</small></div>
      <dl class="detail-list"><dt>Order reference</dt><dd><code>${escape(order.id)}</code></dd><dt>Reserved</dt><dd>${escape(dateTime(order.created_at))} WAT</dd><dt>Reservation deadline</dt><dd>${escape(dateTime(order.expires_at))} WAT</dd><dt>Payment status</dt><dd>${escape(order.provider_status || 'No provider update recorded')}</dd><dt>Record version</dt><dd>${escape(order.version)}</dd></dl>
      <p class="detail-note">${order.status==='pending_payment' ? 'Complete payment before your reservation deadline. Check the latest order status before arranging collection.' : 'Keep this reference with your payment or collection records. A received payment is separate from a fulfilment update.'}</p>
      <div class="detail-actions">${order.status==='pending_payment' ? `<button class="primary" id="pay-order">Pay ${escape(money(order.amount_minor,order.currency))} ${icon('arrow')}</button>` : ''}<button class="secondary" id="copy-reference">Copy reference</button></div>`;
    $('#lookup-dialog').close();
    $('#order-dialog').showModal();
    $('#copy-reference').onclick=async()=>{
      try { await navigator.clipboard.writeText(order.id); notify('Order reference copied.'); }
      catch { notify(`Order reference: ${order.id}`); }
    };
    if ($('#pay-order')) $('#pay-order').onclick=async()=>{
      const button=$('#pay-order'); button.disabled=true; button.textContent='Confirming payment…';
      try { await request(`/api/orders/${encodeURIComponent(order.id)}/pay`,{method:'POST'}); $('#order-dialog').close(); await loadOrders(); notify('Payment recorded. Your order has been updated.'); }
      catch(error) { showError(error); button.disabled=false; button.textContent=`Pay ${money(order.amount_minor,order.currency)}`; }
    };
  } catch(error) {
    if ($('#lookup-dialog').open) { $('#lookup-error').textContent=messages[error.message] || error.message; $('#lookup-error').hidden=false; }
    else showError(error);
  }
}
async function loadWallet() {
  try {
    state.wallet=await request('/api/wallet');
    $('#wallet-balance').textContent=money(state.wallet.balance_minor);
    $('#wallet-entries').innerHTML=state.wallet.entries.map(entry=>`<tr><td>${escape(entry.note)}<small>${escape(entry.id)}</small></td><td><code>${escape(entry.source_ref)}</code></td><td>${escape(dateTime(entry.created_at))} WAT</td><td class="amount-column ${entry.delta_minor>=0?'credit':'debit'}">${entry.delta_minor>=0?'+':'−'}${escape(money(Math.abs(entry.delta_minor)))}</td></tr>`).join('') || '<tr><td colspan="4">No posted transactions.</td></tr>';
  } catch(error) { showError(error); }
}
function switchView(view) {
  const labels={orders:'Orders',wallet:'Wallet',help:'Collection & help'};
  if (!labels[view]) return;
  for (const name of Object.keys(labels)) $(`#${name}-view`).hidden=name!==view;
  for (const button of document.querySelectorAll('.main-nav [data-view]')) {
    button.classList.toggle('active',button.dataset.view===view);
    if (button.dataset.view===view) button.setAttribute('aria-current','page'); else button.removeAttribute('aria-current');
  }
  $('#breadcrumb').textContent=labels[view]; document.title=`HarbourDesk — ${labels[view]}`;
  if (view==='wallet') loadWallet();
}
function downloadCsv(name,columns,rows) {
  // Quote cell contents and prevent a spreadsheet from executing data as formulas.
  const cell=value=>{ if (typeof value==='number' && Number.isFinite(value)) return String(value); let text=String(value ?? ''); if (/^[\s]*[=+@-]/.test(text)) text="'"+text; return '"'+text.replace(/"/g,'""')+'"'; };
  const csv=[columns,...rows].map(row=>row.map(cell).join(',')).join('\r\n');
  const url=URL.createObjectURL(new Blob(['\ufeff',csv],{type:'text/csv;charset=utf-8'}));
  const link=document.createElement('a'); link.href=url; link.download=name; link.click();
  setTimeout(()=>URL.revokeObjectURL(url),1000);
  notify('Your CSV has been saved.');
}
$('#login-form').onsubmit=async event=>{
  event.preventDefault(); const button=$('#signin'); button.disabled=true;
  try {
    await request('/auth/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:$('#email').value,password:$('#password').value})});
    state.user=await request('/api/me'); showAccount(); switchView('orders'); await loadOrders();
  } catch(error) { showError(error); }
  finally { button.disabled=false; }
};
document.addEventListener('click',event=>{
  const account=event.target.closest('[data-account]');
  if (account) { $('#email').value=`${account.dataset.account}@example.test`; $('#password').value='practice-only'; $('#signin').focus(); }
  const view=event.target.closest('[data-view]'); if (view) switchView(view.dataset.view);
  const guide=event.target.closest('[data-guide]'); if (guide) $('#guide-dialog').showModal();
  const open=event.target.closest('[data-open]'); if (open) openOrder(open.dataset.open);
  const filter=event.target.closest('[data-filter]');
  if (filter) {
    state.filter=filter.dataset.filter; state.page=1;
    for (const tab of document.querySelectorAll('[data-filter]')) { const selected=tab===filter; tab.classList.toggle('active',selected); tab.setAttribute('aria-pressed',String(selected)); }
    loadOrders();
  }
});
$('#search-form').onsubmit=event=>{ event.preventDefault(); state.query=$('#search').value; state.page=1; loadOrders(); };
$('#search').addEventListener('search',()=>{ if ($('#search').value==='') { state.query='';state.page=1;loadOrders(); } });
$('#clear-filters').onclick=()=>{ $('#search').value=''; state.query=''; state.page=1; $('[data-filter="all"]').click(); };
$('#page-size').onchange=()=>{ state.pageSize=$('#page-size').value; state.page=1; loadOrders(); };
$('#previous').onclick=()=>{ if (state.page>1) { state.page--; loadOrders(); } };
$('#next').onclick=()=>{ state.page++; loadOrders(); };
$('#refresh').onclick=async()=>{ await loadOrders(); if (!$('#wallet-view').hidden) await loadWallet(); };
$('#lookup').onclick=()=>{ $('#lookup-error').hidden=true; $('#lookup-reference').value=''; $('#lookup-dialog').showModal(); };
$('#lookup-form').onsubmit=event=>{event.preventDefault(); $('#lookup-error').hidden=true; openOrder($('#lookup-reference').value);};
$('#signout').onclick=async()=>{
  try { await request('/auth/logout',{method:'POST'}); state.requestId++; state.user=null; state.all=[];state.visible=[];state.wallet=null;state.filter='all';state.query='';state.page=1;state.pageSize='all'; $('#page-size').value='all'; $('#search').value=''; document.querySelectorAll('[data-filter]').forEach(button=>{ const active=button.dataset.filter==='all';button.classList.toggle('active',active);button.setAttribute('aria-pressed',String(active)); }); showSignIn(); }
  catch(error) { showError(error); }
};
$('#export-orders').onclick=()=>downloadCsv('harbourdesk-orders.csv',['order_id','status','amount_minor','currency','created_at','expires_at','version'],state.visible.map(o=>[o.id,o.status,o.amount_minor,o.currency,o.created_at,o.expires_at,o.version]));
$('#export-wallet').onclick=()=>{if(state.wallet) downloadCsv('harbourdesk-wallet-ledger.csv',['entry_id','source_ref','delta_minor','created_at','note'],state.wallet.entries.map(e=>[e.id,e.source_ref,e.delta_minor,e.created_at,e.note]));};
setInterval(updateCountdowns,1000);
(async()=>{
  try { state.user=await request('/api/me'); showAccount(); switchView('orders'); await loadOrders(); }
  catch(error) { if(error.message==='authentication_required') showSignIn(); else showError(error); }
})();
