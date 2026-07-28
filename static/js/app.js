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

  openEnquireModal(categoryName = 'Other Plans') {
    this.currentCategory = categoryName;
    const modal = document.getElementById('enquireModal');
    const modalTitle = document.getElementById('enquireModalTitle');
    const reqTextarea = document.getElementById('enquireReq');
    const msgBox = document.getElementById('enquireMsg');

    if (modalTitle) modalTitle.innerText = `Enquire about ${categoryName}`;
    if (reqTextarea) {
      reqTextarea.placeholder = `Briefly describe what you need for ${categoryName}...`;
    }
    if (msgBox) msgBox.style.display = 'none';

    if (modal) modal.style.display = 'flex';
  },

  closeEnquireModal() {
    const modal = document.getElementById('enquireModal');
    if (modal) modal.style.display = 'none';
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

  async submitEnquireForm() {
    const name = document.getElementById('enquireName')?.value || '';
    const phone = document.getElementById('enquirePhone')?.value || '';
    const req = document.getElementById('enquireReq')?.value || '';
    const category = this.currentCategory;
    const msgBox = document.getElementById('enquireMsg');

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
      window.location.href = `mailto:suman@nidhiiq.com?subject=${mailSubject}&body=${mailBody}`;

      setTimeout(() => {
        this.closeEnquireModal();
        if (msgBox) msgBox.style.display = 'none';
        document.getElementById('enquireForm')?.reset();
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
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
