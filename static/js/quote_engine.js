/* NidhiIQ Interactive Quote Engine & Calculators */

const QuoteEngine = {
  // Term Life Quote Generator
  async generateTermQuotes() {
    const age = parseInt(document.getElementById('termAge')?.value || 30);
    const gender = document.getElementById('termGender')?.value || 'male';
    const tobacco = document.getElementById('termTobacco')?.value === 'true';
    const sumAssured = parseFloat(document.getElementById('termSumAssured')?.value || 10000000);
    const policyTerm = parseInt(document.getElementById('termPolicyTerm')?.value || 30);
    const income = parseFloat(document.getElementById('termIncome')?.value || 1000000);

    const resultsContainer = document.getElementById('termQuotesResults');
    if (!resultsContainer) return;

    resultsContainer.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 30px;"><div class="spinner"></div> Calculating live quotes from top Indian insurers...</div>`;

    try {
      const response = await fetch('/api/v1/quotes/term-life', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          age: age,
          gender: gender,
          tobacco: tobacco,
          annual_income: income,
          sum_assured: sumAssured,
          policy_term: policyTerm
        })
      });

      const quotes = await response.json();
      this.renderTermQuotes(quotes, resultsContainer);
    } catch (err) {
      console.error('Error fetching term quotes:', err);
      resultsContainer.innerHTML = `<div style="grid-column:1/-1; color: red;">Failed to load live quotes. Please check your connection.</div>`;
    }
  },

  renderTermQuotes(quotes, container) {
    if (!quotes || quotes.length === 0) {
      container.innerHTML = `<p>No quotes available for selected criteria.</p>`;
      return;
    }

    container.innerHTML = quotes.map(q => `
      <div class="quote-card">
        <div class="quote-header">
          <div>
            <div class="quote-provider">${q.provider_name}</div>
            <div style="font-size: 0.82rem; color: #64748b;">${q.title}</div>
          </div>
          ${q.badge ? `<span style="background:#dbeafe; color:#1e40af; font-size:0.7rem; font-weight:700; padding:2px 8px; border-radius:12px;">${q.badge}</span>` : ''}
        </div>
        <div style="margin: 12px 0;">
          <div class="quote-price">₹${q.monthly_premium.toLocaleString('en-IN')} <span>/ month</span></div>
          <div style="font-size: 0.8rem; color: #059669; font-weight: 600;">₹${q.annual_premium.toLocaleString('en-IN')} annual premium</div>
          <div style="font-size: 0.78rem; color: #0d9488; margin-top: 4px;">Save up to ₹${q.tax_savings_80c.toLocaleString('en-IN')} under Sec 80C</div>
        </div>
        <div style="font-size: 0.8rem; color: #475569; margin-bottom: 12px;">
          <strong>Claim Settlement Ratio:</strong> ${q.claim_settlement_ratio}%
        </div>
        <ul style="list-style:none; font-size:0.78rem; color:#475569; margin-bottom:16px;">
          ${q.features.slice(0, 2).map(f => `<li>✓ ${f}</li>`).join('')}
        </ul>
        <div style="display:flex; gap:8px;">
          <button onclick="App.openAdvisorModal('Term Life Insurance - ${q.provider_name}')" class="btn btn-primary" style="flex:1; font-size:0.82rem; padding:8px 12px;">Get Quote Policy</button>
          <button onclick="App.comparePolicy('${q.provider_name}', '${q.title}', '${q.monthly_premium}', '${q.claim_settlement_ratio}')" class="btn btn-outline-light" style="color:#0f172a; border-color:#cbd5e1; font-size:0.82rem; padding:8px 12px;">Compare</button>
        </div>
      </div>
    `).join('');
  },

  // Health Insurance Quote Generator
  async generateHealthQuotes() {
    const age = parseInt(document.getElementById('healthAge')?.value || 32);
    const coverType = document.getElementById('healthCoverType')?.value || 'individual';
    const sumInsured = parseFloat(document.getElementById('healthSumInsured')?.value || 1000000);
    const cityTier = document.getElementById('healthCityTier')?.value || 'tier1';
    const preExisting = document.getElementById('healthPreExisting')?.value === 'true';

    const resultsContainer = document.getElementById('healthQuotesResults');
    if (!resultsContainer) return;

    resultsContainer.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 30px;"><div class="spinner"></div> Finding best health policies...</div>`;

    try {
      const response = await fetch('/api/v1/quotes/health', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          age: age,
          cover_type: coverType,
          adults_count: coverType === 'family' ? 2 : 1,
          children_count: coverType === 'family' ? 1 : 0,
          sum_insured: sumInsured,
          city_tier: cityTier,
          pre_existing_disease: preExisting
        })
      });

      const quotes = await response.json();
      this.renderHealthQuotes(quotes, resultsContainer);
    } catch (err) {
      console.error('Error fetching health quotes:', err);
      resultsContainer.innerHTML = `<div style="grid-column:1/-1; color: red;">Failed to load health quotes.</div>`;
    }
  },

  renderHealthQuotes(quotes, container) {
    if (!quotes || quotes.length === 0) {
      container.innerHTML = `<p>No health policies available.</p>`;
      return;
    }

    container.innerHTML = quotes.map(q => `
      <div class="quote-card">
        <div class="quote-header">
          <div>
            <div class="quote-provider">${q.provider_name}</div>
            <div style="font-size: 0.82rem; color: #64748b;">${q.title}</div>
          </div>
          ${q.badge ? `<span style="background:#dcfce7; color:#15803d; font-size:0.7rem; font-weight:700; padding:2px 8px; border-radius:12px;">${q.badge}</span>` : ''}
        </div>
        <div style="margin: 12px 0;">
          <div class="quote-price">₹${q.monthly_premium.toLocaleString('en-IN')} <span>/ month</span></div>
          <div style="font-size: 0.8rem; color: #059669; font-weight: 600;">Sum Insured: ₹${(q.sum_insured / 100000).toFixed(0)} Lakhs</div>
          <div style="font-size: 0.78rem; color: #0d9488; margin-top: 4px;">Save tax up to ₹${q.tax_savings_80d.toLocaleString('en-IN')} under Sec 80D</div>
        </div>
        <div style="font-size: 0.8rem; color: #475569; margin-bottom: 12px;">
          <strong>Cashless Hospitals:</strong> ${q.network_hospitals.toLocaleString('en-IN')}+ | <strong>CSR:</strong> ${q.claim_settlement_ratio}%
        </div>
        <ul style="list-style:none; font-size:0.78rem; color:#475569; margin-bottom:16px;">
          ${q.features.slice(0, 2).map(f => `<li>✓ ${f}</li>`).join('')}
        </ul>
        <div style="display:flex; gap:8px;">
          <button onclick="App.openAdvisorModal('Health Insurance - ${q.provider_name}')" class="btn btn-primary" style="flex:1; font-size:0.82rem; padding:8px 12px;">Buy Cashless Policy</button>
          <button onclick="App.comparePolicy('${q.provider_name}', '${q.title}', '${q.monthly_premium}', '${q.claim_settlement_ratio}')" class="btn btn-outline-light" style="color:#0f172a; border-color:#cbd5e1; font-size:0.82rem; padding:8px 12px;">Compare</button>
        </div>
      </div>
    `).join('');
  },

  // SIP Wealth Calculator
  async calculateSIP() {
    const monthlyAmt = parseFloat(document.getElementById('sipMonthlyAmt')?.value || 5000);
    const tenureYears = parseInt(document.getElementById('sipTenure')?.value || 15);
    const returnRate = parseFloat(document.getElementById('sipReturnRate')?.value || 12);

    const displayInvested = document.getElementById('sipTotalInvested');
    const displayReturns = document.getElementById('sipEstReturns');
    const displayTotal = document.getElementById('sipTotalValue');
    const fundsContainer = document.getElementById('sipRecommendedFunds');

    try {
      const response = await fetch('/api/v1/quotes/sip', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          monthly_investment: monthlyAmt,
          tenure_years: tenureYears,
          expected_return_rate: returnRate
        })
      });

      const res = await response.json();
      if (displayInvested) displayInvested.innerText = '₹' + res.total_invested.toLocaleString('en-IN');
      if (displayReturns) displayReturns.innerText = '₹' + res.estimated_returns.toLocaleString('en-IN');
      if (displayTotal) displayTotal.innerText = '₹' + res.total_value.toLocaleString('en-IN');

      if (fundsContainer && res.recommended_funds) {
        fundsContainer.innerHTML = res.recommended_funds.map(f => `
          <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px 16px; border-radius:10px; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <strong style="color:#0f172a; font-size:0.92rem;">${f.fund_name}</strong>
              <div style="font-size:0.78rem; color:#64748b;">Category: ${f.category} | ${f.rating}</div>
            </div>
            <div style="text-align:right;">
              <div style="color:#059669; font-weight:800; font-size:1rem;">${f.cagr_3yr} 3Y Return</div>
              <button onclick="App.openAdvisorModal('Mutual Fund - ${f.fund_name}')" class="btn btn-gold" style="padding:4px 10px; font-size:0.75rem; margin-top:4px;">Start SIP</button>
            </div>
          </div>
        `).join('');
      }
    } catch (err) {
      console.error('Error calculating SIP:', err);
    }
  }
};
