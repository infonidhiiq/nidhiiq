/* NidhiIQ Main Application Logic */

const App = {
  currentCategory: 'Other Plans',
  currentHeroSlide: 0,
  heroSlideTimer: null,

  init() {
    this.setupEventListeners();
    this.initHeroSlider();
  },

  initHeroSlider() {
    const track = document.getElementById('heroSliderTrack');
    if (!track) return;

    this.startHeroSlideAutoPlay();

    const wrapper = document.querySelector('.hero-slider-wrapper');
    if (wrapper) {
      wrapper.addEventListener('mouseenter', () => this.stopHeroSlideAutoPlay());
      wrapper.addEventListener('mouseleave', () => this.startHeroSlideAutoPlay());
    }
  },

  goToHeroSlide(index, event = null) {
    if (event) event.stopPropagation();
    const track = document.getElementById('heroSliderTrack');
    const dots = document.querySelectorAll('.hero-dot');
    if (!track) return;

    this.currentHeroSlide = (index + 2) % 2;
    track.style.transform = `translateX(-${this.currentHeroSlide * 100}%)`;

    dots.forEach((dot, idx) => {
      if (idx === this.currentHeroSlide) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  },

  nextHeroSlide(event = null) {
    this.goToHeroSlide(this.currentHeroSlide + 1, event);
  },

  prevHeroSlide(event = null) {
    this.goToHeroSlide(this.currentHeroSlide - 1, event);
  },

  startHeroSlideAutoPlay() {
    this.stopHeroSlideAutoPlay();
    this.heroSlideTimer = setInterval(() => {
      this.nextHeroSlide();
    }, 3500);
  },

  stopHeroSlideAutoPlay() {
    if (this.heroSlideTimer) {
      clearInterval(this.heroSlideTimer);
      this.heroSlideTimer = null;
    }
  },

  setupEventListeners() {
    // Enquire modal form
    const enquireForm = document.getElementById('enquireForm');
    if (enquireForm) {
      enquireForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await this.submitEnquireForm();
      });
    }

    // Claim submit form
    const claimForm = document.getElementById('claimSubmitForm');
    if (claimForm) {
      claimForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        await this.submitClaimRequest();
      });
    }
  },

  top14Categories: [
    'Term Life Insurance',
    'Free of Cost Term Life Insurance',
    'Health Insurance',
    'Investment Plans',
    'Motor Insurance',
    'Term Plans',
    'Guaranteed Return Plans',
    'Child Savings Plans',
    'Family Health Insurance',
    'Travel Insurance',
    'Retirement Plans',
    'Employee Group Health Insurance',
    'Home Insurance',
    'Family Office',
    'Real Estate',
    'Loan Solutions',
    'About NidhiIQ',
    'Pet Insurance Protection',
    'Child Future Savings'
  ],

  renderRichModalContent(categoryName) {
    const leftCol = document.getElementById('enquireModalLeftCol');
    if (!leftCol) return;

    const norm = (categoryName || '').toString().trim().toLowerCase();

    if (norm === 'health insurance' || norm === 'family health insurance') {
      leftCol.innerHTML = `
        <div style="display:inline-flex; align-items:center; gap:8px; background:#e0e7ff; color:#3730a3; padding:6px 14px; border-radius:20px; font-size:0.82rem; font-weight:700; margin-bottom:14px;">
          <span>🛡️</span> <span>Secure Today. Protect Tomorrow.</span>
        </div>
        <h2 style="font-size:1.95rem; font-weight:900; color:#0f172a; margin:0 0 10px; line-height:1.2; letter-spacing:-0.5px;">Health Insurance – Healthier You, <span style="color:#15803d;">Happier Life</span></h2>
        <p style="font-size:0.92rem; color:#475569; margin:0 0 24px; line-height:1.5;">Protect your family from medical costs and enjoy peace of mind.</p>

        <!-- 4 Feature Pillars Grid -->
        <div class="modal-features-grid-v2" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; margin-bottom:24px; text-align:center;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_rising_costs.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2; margin-bottom:2px;">Rising Costs</div>
            <div style="font-size:0.73rem; color:#64748b; line-height:1.2;">Covers increasing medical expenses.</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_fin_sec.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2; margin-bottom:2px;">Financial Security</div>
            <div style="font-size:0.73rem; color:#64748b; line-height:1.2;">Pre &amp; post hospitalization.</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_cashless.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2; margin-bottom:2px;">Cashless Treatment</div>
            <div style="font-size:0.73rem; color:#64748b; line-height:1.2;">Wide network of hospitals.</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_peace.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2; margin-bottom:2px;">Peace of Mind</div>
            <div style="font-size:0.73rem; color:#64748b; line-height:1.2;">Prepared for emergencies.</div>
          </div>
        </div>

        <!-- Peach Bottom Box -->
        <div class="modal-peach-box-v2" style="background:#fff7ed; border:1px solid #ffedd5; border-radius:16px; padding:16px 18px; display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; text-align:center;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_cov_hospital.png?v=1" style="width:48px; height:48px; object-fit:contain; margin-bottom:4px;">
            <div style="font-weight:800; font-size:0.8rem; color:#0f172a; margin-bottom:2px;">What it Covers:</div>
            <div style="font-size:0.72rem; color:#475569; line-height:1.25;">Hospitalization Expenses, Day Care, Ambulance Charges.</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_cov_medicine.png?v=1" style="width:48px; height:48px; object-fit:contain; margin-bottom:4px;">
            <div style="font-weight:800; font-size:0.8rem; color:#0f172a; margin-bottom:2px;">What it Covers:</div>
            <div style="font-size:0.72rem; color:#475569; line-height:1.25;">Expenses, Pill bottles.</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/health_cov_ambulance.png?v=1" style="width:48px; height:48px; object-fit:contain; margin-bottom:4px;">
            <div style="font-weight:800; font-size:0.8rem; color:#0f172a; margin-bottom:2px;">Ambulance</div>
            <div style="font-size:0.72rem; color:#475569; line-height:1.25;">Ambulance Charges.</div>
          </div>
        </div>
      `;
    } else if (norm === 'investment plans') {
      leftCol.innerHTML = `
        <div style="display:inline-flex; align-items:center; gap:8px; background:#e0e7ff; color:#3730a3; padding:6px 14px; border-radius:20px; font-size:0.82rem; font-weight:700; margin-bottom:14px;">
          <span>📈</span> <span>Smart Today. Secure Tomorrow.</span>
        </div>
        <h2 style="font-size:1.95rem; font-weight:900; color:#0f172a; margin:0 0 10px; line-height:1.2; letter-spacing:-0.5px;">Investment Plans – Smart Today, <span style="color:#15803d;">Secure Tomorrow</span></h2>
        <p style="font-size:0.92rem; color:#475569; margin:0 0 24px; line-height:1.5;">Build wealth and secure your family's future with high-return investment plans.</p>

        <h3 style="font-size:1.05rem; font-weight:800; color:#0f172a; text-align:center; margin:0 0 16px;">Popular Investment Options</h3>

        <div class="modal-features-grid-v2" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; text-align:center;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/inv_mutual_funds.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a;">Mutual Funds</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/inv_sip.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a;">SIP Plans</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/inv_retirement.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a;">Retirement Plans</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/inv_child.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a;">Child Plans</div>
          </div>
        </div>
      `;
    } else if (norm === 'motor insurance') {
      leftCol.innerHTML = `
        <div style="display:inline-flex; align-items:center; gap:8px; background:#e0e7ff; color:#3730a3; padding:6px 14px; border-radius:20px; font-size:0.82rem; font-weight:700; margin-bottom:14px;">
          <span>🚗</span> <span>Drive Worry-Free.</span>
        </div>
        <h2 style="font-size:1.95rem; font-weight:900; color:#0f172a; margin:0 0 10px; line-height:1.2; letter-spacing:-0.5px;">Motor Insurance – <span style="color:#15803d;">Drive Worry-Free</span></h2>
        <p style="font-size:0.92rem; color:#475569; margin:0 0 24px; line-height:1.5;">Complete protection for your vehicle with cashless garage networks.</p>

        <h3 style="font-size:1.05rem; font-weight:800; color:#0f172a; text-align:center; margin:0 0 16px;">Choose the Right Coverage</h3>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:14px; padding:14px;">
            <div style="font-weight:800; font-size:0.88rem; color:#0f172a; margin-bottom:4px;">Third Party Insurance</div>
            <div style="font-size:0.78rem; color:#64748b; line-height:1.3;">Covers legal liability for injury, death or property damage.</div>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:14px; padding:14px;">
            <div style="font-weight:800; font-size:0.88rem; color:#0f172a; margin-bottom:4px;">Comprehensive Insurance</div>
            <div style="font-size:0.78rem; color:#64748b; line-height:1.3;">Covers vehicle damage and third party liability for complete protection.</div>
          </div>
        </div>
      `;
    } else if (norm === 'guaranteed return plans' || norm === 'guaranteed return plan') {
      leftCol.innerHTML = `
        <div style="display:inline-flex; align-items:center; gap:8px; background:#e0e7ff; color:#3730a3; padding:6px 14px; border-radius:20px; font-size:0.82rem; font-weight:700; margin-bottom:14px;">
          <span>🛡️</span> <span>Secure Today. Assured Tomorrow.</span>
        </div>
        <h2 style="font-size:1.95rem; font-weight:900; color:#0f172a; margin:0 0 10px; line-height:1.2; letter-spacing:-0.5px;">Guaranteed Return Plans – <span style="color:#15803d;">Secure Returns, Assured Future</span></h2>
        <p style="font-size:0.92rem; color:#475569; margin:0 0 24px; line-height:1.5;">Enjoy assured returns with zero market risk and build a better future for your family.</p>

        <h3 style="font-size:1.05rem; font-weight:800; color:#0f172a; text-align:center; margin:0 0 16px;">How It Works</h3>
        <div class="modal-steps-flex-v2" style="display:flex; align-items:center; justify-content:space-between; gap:6px;">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_choose.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">1</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Choose Plan</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_pay.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">2</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Pay Premium</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_protected.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">3</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Enjoy Assured Returns</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_family.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">4</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Secure Your Future</div>
          </div>
        </div>
      `;
    } else {
      // Default Term Plan Layout
      leftCol.innerHTML = `
        <div style="display:inline-flex; align-items:center; gap:8px; background:#e0e7ff; color:#3730a3; padding:6px 14px; border-radius:20px; font-size:0.82rem; font-weight:700; margin-bottom:14px;">
          <span>🛡️</span> <span>Secure Today. Protect Tomorrow.</span>
        </div>
        <h2 style="font-size:1.95rem; font-weight:900; color:#0f172a; margin:0 0 10px; line-height:1.2; letter-spacing:-0.5px;">Term Plan – Life Cover That <span style="color:#15803d;">Protects Their Tomorrow</span></h2>
        <p style="font-size:0.92rem; color:#475569; margin:0 0 24px; line-height:1.5;">Financial Protection for Your Family: Secure their future with Term Life Insurance.</p>

        <div class="modal-features-grid-v2" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; margin-bottom:24px; text-align:center;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/feat_security.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2;">Financial<br>Security</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/feat_cover.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2;">High Cover,<br>Low Premium</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/feat_simple.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2;">Simple &amp;<br>Transparent</div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <img src="/static/images/modal_assets/feat_tax.png?v=1" style="width:64px; height:64px; object-fit:contain; margin-bottom:6px;">
            <div style="font-weight:800; font-size:0.82rem; color:#0f172a; line-height:1.2;">Tax<br>Benefits</div>
          </div>
        </div>

        <h3 style="font-size:1.05rem; font-weight:800; color:#0f172a; text-align:center; margin:0 0 16px;">How It Works</h3>
        <div class="modal-steps-flex-v2" style="display:flex; align-items:center; justify-content:space-between; gap:6px;">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_choose.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">1</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Choose Plan</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_pay.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">2</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Pay Premium</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_protected.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">3</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Stay Protected</div>
          </div>
          <div class="modal-steps-arrow-v2" style="color:#cbd5e1; font-weight:800; font-size:1.1rem;">➔</div>
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
            <div style="position:relative; margin-bottom:6px;">
              <img src="/static/images/modal_assets/step_family.png?v=2" style="width:58px; height:58px; border-radius:50%; object-fit:cover;">
              <span style="position:absolute; top:-4px; left:-4px; background:#15803d; color:#ffffff; width:20px; height:20px; border-radius:50%; font-size:0.75rem; font-weight:800; display:flex; align-items:center; justify-content:center;">4</span>
            </div>
            <div style="font-size:0.78rem; font-weight:700; color:#1e293b;">Family Secured</div>
          </div>
        </div>
      `;
    }
  },

  openEnquireModal(categoryName = 'Other Plans') {
    this.currentCategory = categoryName;

    const norm = (categoryName || '').toString().trim().toLowerCase();

    const isHealth = norm === 'health insurance' || norm === 'family health insurance';
    const isInvestment = norm === 'investment plans';
    const isMotor = norm === 'motor insurance';
    const isGuaranteed = norm === 'guaranteed return plans' || norm === 'guaranteed return plan';
    const isTerm = norm === 'term life insurance' || norm === 'term plans' || norm === 'term plan';

    if (isHealth || isInvestment || isMotor || isGuaranteed || isTerm) {
      // Use Rich Modern 2-Column Modal ONLY for the 5 custom requested products!
      const modal = document.getElementById('enquireModal');
      const simpleModal = document.getElementById('simpleEnquireModal');
      if (simpleModal) simpleModal.style.display = 'none';

      const modalTitle = document.getElementById('enquireModalTitle');
      const heroImg = document.getElementById('enquireModalHeroImg');
      const reqTextarea = document.getElementById('enquireReq');
      const msgBox = document.getElementById('enquireMsg');

      if (modalTitle) modalTitle.innerText = `Enquire about ${categoryName}`;

      // Dynamically render product specific left column content
      this.renderRichModalContent(categoryName);

      if (isHealth) {
        if (heroImg) heroImg.src = '/static/images/modal_assets/health_hero.png?v=1';
      } else if (isInvestment) {
        if (heroImg) heroImg.src = '/static/images/modal_assets/inv_hero.png?v=1';
      } else if (isMotor) {
        if (heroImg) heroImg.src = '/static/images/modal_assets/motor_hero.png?v=1';
      } else if (isGuaranteed) {
        if (heroImg) heroImg.src = '/static/images/modal_assets/gr_hero.png?v=1';
      } else if (isTerm) {
        if (heroImg) heroImg.src = '/static/images/modal_assets/term_hero.png?v=1';
      }

      if (reqTextarea) reqTextarea.placeholder = 'Requirement';
      if (msgBox) msgBox.style.display = 'none';
      if (modal) modal.style.display = 'flex';

    } else {
      // Use Standard / Previous Simple Query Form Modal (Name, Number, Query) for ALL other icons!
      const modal = document.getElementById('enquireModal');
      const simpleModal = document.getElementById('simpleEnquireModal');
      if (modal) modal.style.display = 'none';

      const simpleTitle = document.getElementById('simpleEnquireTitle');
      const simpleReq = document.getElementById('simpleEnquireReq');
      const simpleMsg = document.getElementById('simpleEnquireMsg');

      if (simpleTitle) simpleTitle.innerText = `Enquire about ${categoryName}`;
      if (simpleReq) simpleReq.placeholder = `Briefly describe what you need for ${categoryName}...`;
      if (simpleMsg) simpleMsg.style.display = 'none';

      if (simpleModal) simpleModal.style.display = 'flex';
    }
  },

  closeEnquireModal() {
    const modal = document.getElementById('enquireModal');
    const simpleModal = document.getElementById('simpleEnquireModal');
    if (modal) modal.style.display = 'none';
    if (simpleModal) simpleModal.style.display = 'none';
  },

  openAdvisorModal(categoryName) {
    this.openEnquireModal(categoryName);
  },

  closeAdvisorModal() {
    this.closeEnquireModal();
  },

  updateCharCount(textarea) {
    const counter = document.getElementById('charCounter');
    if (counter) {
      counter.innerText = `${textarea.value.length}/500`;
    }
  },

  async submitEnquireForm(isSimple = false) {
    const nameId = isSimple ? 'simpleEnquireName' : 'enquireName';
    const phoneId = isSimple ? 'simpleEnquirePhone' : 'enquirePhone';
    const reqId = isSimple ? 'simpleEnquireReq' : 'enquireReq';
    const msgId = isSimple ? 'simpleEnquireMsg' : 'enquireMsg';

    const name = document.getElementById(nameId)?.value || '';
    const phone = document.getElementById(phoneId)?.value || '';
    const req = document.getElementById(reqId)?.value || '';
    const category = this.currentCategory;
    const msgBox = document.getElementById(msgId);

    try {
      // 1. Submit lead to Python FastAPI backend
      const res = await fetch('/api/v1/leads/advisor-callback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          full_name: name,
          phone_number: `+91${phone}`,
          email: '',
          interested_category: `${category} — Requirement: ${req}`,
          preferred_time: 'Immediate WhatsApp'
        })
      });
      const data = await res.json();

      if (msgBox) {
        msgBox.style.display = 'block';
        msgBox.innerHTML = `
          <div style="background:#ecfdf5; border:1px solid #10b981; padding:10px 14px; border-radius:12px; color:#065f46; font-size:0.88rem;">
            ✓ ${data.message} Opening WhatsApp & Email...
          </div>
        `;
      }

      // 2. Open WhatsApp chat with pre-filled message
      const waText = encodeURIComponent(`Hello NidhiIQ Advisor, I am enquiring about *${category}*.\nName: ${name}\nPhone: +91 ${phone}\nRequirement: ${req}`);
      window.open(`https://wa.me/916361839979?text=${waText}`, '_blank');

      // 3. Open mailto email draft
      const mailSubject = encodeURIComponent(`Enquiry for ${category} — NidhiIQ`);
      const mailBody = encodeURIComponent(`Name: ${name}\nPhone: +91 ${phone}\nCategory: ${category}\nRequirement: ${req}`);
      window.location.href = `mailto:support@nidhiiq.com?subject=${mailSubject}&body=${mailBody}`;

      setTimeout(() => {
        this.closeEnquireModal();
        if (msgBox) msgBox.style.display = 'none';
        document.getElementById('enquireForm')?.reset();
        document.getElementById('simpleEnquireForm')?.reset();
        this.updateCharCount({ value: '' });
      }, 2500);

    } catch (err) {
      console.error('Error submitting enquiry:', err);
      if (msgBox) {
        msgBox.style.display = 'block';
        msgBox.innerHTML = `<span style="color:red;">Error submitting enquiry. Please try again.</span>`;
      }
    }
  },

  openClaimsModal() {
    const modal = document.getElementById('claimsModal');
    if (modal) modal.style.display = 'flex';
  },

  closeClaimsModal() {
    const modal = document.getElementById('claimsModal');
    if (modal) modal.style.display = 'none';
  },

  async submitClaimRequest() {
    const insuredName = document.getElementById('claimInsuredName')?.value;
    const policyNum = document.getElementById('claimPolicyNum')?.value;
    const phone = document.getElementById('claimPhone')?.value;
    const amount = parseFloat(document.getElementById('claimAmount')?.value || 0);
    const resultBox = document.getElementById('claimResultMsg');

    try {
      const res = await fetch('/api/v1/claims/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          insured_name: insuredName,
          policy_number: policyNum,
          phone_number: phone,
          category: 'Claims Assistance',
          claim_amount: amount
        })
      });
      const data = await res.json();
      if (resultBox) {
        resultBox.style.display = 'block';
        resultBox.innerHTML = `
          <div style="background:#ecfdf5; border:1px solid #10b981; padding:12px; border-radius:8px; color:#065f46;">
            <strong>Ticket Created: ${data.ticket_number}</strong><br/>
            ${data.message}
          </div>
        `;
      }
    } catch (err) {
      console.error(err);
    }
  },

  openWhatsAppChat() {
    window.open('https://wa.me/916361839979?text=Hello%20NidhiIQ%20Advisor%2C%20I%20would%20like%20to%20get%20assistance%20with%20insurance%2C%20real%20estate%2C%20loans%2C%20or%20family%20office%20services.', '_blank');
  },

  scrollReviews(direction) {
    const track = document.getElementById('reviewsScrollTrack');
    if (!track) return;
    const scrollAmount = 340;
    if (direction === 'left') {
      track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    } else {
      track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
