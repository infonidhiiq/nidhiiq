import re
import os

html_paths = [r'templates/index.html', r'index.html']

categories_data = [
    {
        'title': 'MUTUAL FUNDS',
        'icon': '📊',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Flexi Cap', '/static/images/mutual_funds_icons/flexi_cap.png'),
            ('Large Cap', '/static/images/mutual_funds_icons/large_cap.png'),
            ('Large & Mid Cap', '/static/images/mutual_funds_icons/large_and_mid_cap.png'),
            ('Mid Cap', '/static/images/mutual_funds_icons/mid_cap.png'),
            ('Small Cap', '/static/images/mutual_funds_icons/small_cap.png'),
            ('Multi Cap', '/static/images/mutual_funds_icons/multi_cap.png'),
            ('Contra Fund', '/static/images/mutual_funds_icons/contra_fund.png')
        ]
    },
    {
        'title': 'LOAN SOLUTIONS',
        'icon': '🏦',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Home Loan', '/static/images/loan_icons/home_loan.png'),
            ('Home Loan BT', '/static/images/loan_icons/home_loan_bt.png'),
            ('Loan Against Property', '/static/images/loan_icons/loan_against_property.png'),
            ('Personal Loan', '/static/images/loan_icons/personal_loan.png'),
            ('Car Loan', '/static/images/loan_icons/car_loan.png'),
            ('Two Wheeler Loan', '/static/images/loan_icons/two_wheeler_loan.png'),
            ('Education Loan', '/static/images/loan_icons/education_loan.png'),
            ('Credit Card', '/static/images/loan_icons/credit_card.png'),
            ('Business Loan', '/static/images/loan_icons/business_loan.png'),
            ('MSME Loan', '/static/images/loan_icons/msme_loan.png'),
            ('Working Capital Loan', '/static/images/loan_icons/working_capital_loan.png'),
            ('Equipment / Machinery Loan', '/static/images/loan_icons/equipment_machinery_loan.png'),
            ('Professional Loan', '/static/images/loan_icons/professional_loan.png'),
            ('Gold Loan', '/static/images/loan_icons/gold_loan.png')
        ]
    },
    {
        'title': 'PERSONAL INSURANCE',
        'icon': '🛡️',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Free of Cost Term Life Insurance', '/static/images/grouped_icons/free_term_life.png'),
            ('Term Plans with Return of Premium', '/static/images/grouped_icons/term_plans_rop.png'),
            ('Term Insurance (Women)', '/static/images/grouped_icons/term_insurance_women.png'),
            ('Term Life Insurance (Self Employed)', '/static/images/grouped_icons/term_life_self_employed.png'),
            ('Term Life Insurance (NRIs)', '/static/images/grouped_icons/term_life_nri_global.png'),
            ('Home Loan Insurance', '/static/images/grouped_icons/home_loan_insurance.png'),
            ('Dollar Based Term Plan', '/static/images/grouped_icons/dollar_term_plan.png'),
            ('Term Insurance for Diabetic', '/static/images/grouped_icons/term_insurance_diabetic.png'),
            ('Term Insurance for Non-Smokers', '/static/images/grouped_icons/term_insurance_non_smokers.png'),
            ('Term Insurance for Doctors', '/static/images/grouped_icons/term_insurance_doctors.png'),
            ('Term Insurance for Salaried Professionals', '/static/images/grouped_icons/term_insurance_salaried.png'),
            ('Term Plan with Critical Illness', '/static/images/grouped_icons/term_plan_critical_illness.png'),
            ('Family Protection Plan', '/static/images/grouped_icons/family_protection_plan.png'),
            ('Instant Online Term Plan', '/static/images/grouped_icons/instant_online_term_plan.png')
        ]
    },
    {
        'title': 'INVESTMENT PLANS',
        'icon': '📈',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('LIC Plans', '/static/images/grouped_icons/lic_plans.png'),
            ('Investment', '/static/images/grouped_icons/investment_general.png'),
            ('Child Savings Plan', '/static/images/grouped_icons/child_savings_plan.png'),
            ('Guaranteed Return Plan', '/static/images/grouped_icons/guaranteed_return_plan.png'),
            ('Retirement Plan', '/static/images/grouped_icons/retirement_plan.png'),
            ('Tax Saving Investment', '/static/images/grouped_icons/tax_saving_investment.png'),
            ('Pension For Life', '/static/images/grouped_icons/pension_for_life.png'),
            ('Smart Deposit', '/static/images/grouped_icons/smart_deposit.png'),
            ('ULIPs', '/static/images/grouped_icons/ulips.png'),
            ('Dollar Based Investment Plan', '/static/images/grouped_icons/dollar_investment_plan.png'),
            ('Mutual Funds', '/static/images/grouped_icons/mutual_funds.png'),
            ('Sovereign Gold Bonds', '/static/images/grouped_icons/sovereign_gold_bonds.png'),
            ('Real Estate Investment', '/static/images/grouped_icons/real_estate_investment.png'),
            ('NPS (National Pension System)', '/static/images/grouped_icons/nps_national_pension_system.png')
        ]
    },
    {
        'title': 'OTHER PLANS',
        'icon': '🚗',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Car Insurance', '/static/images/grouped_icons/car_insurance.png'),
            ('2 Wheeler Insurance', '/static/images/grouped_icons/two_wheeler_insurance.png'),
            ('Health Insurance', '/static/images/grouped_icons/health_insurance.png'),
            ('Life Insurance', '/static/images/grouped_icons/life_insurance.png'),
            ('Travel Insurance', '/static/images/grouped_icons/travel_insurance.png'),
            ('Home Insurance', '/static/images/grouped_icons/home_insurance.png'),
            ('Tax Insurance', '/static/images/grouped_icons/tax_insurance.png'),
            ('Commercial Vehicle', '/static/images/grouped_icons/commercial_vehicle.png'),
            ('Employee Group Health Insurance', '/static/images/grouped_icons/employee_group_health.png'),
            ('Corporate Insurance', '/static/images/grouped_icons/corporate_insurance.png'),
            ('Pet Insurance', '/static/images/grouped_icons/pet_insurance.png'),
            ('Personal Cyber Insurance', '/static/images/grouped_icons/personal_cyber_insurance.png'),
            ('Liability Insurance', '/static/images/grouped_icons/liability_insurance.png'),
            ('Workmen Compensation', '/static/images/grouped_icons/workmen_compensation.png')
        ]
    },
    {
        'title': 'EMPLOYEE BENEFITS',
        'icon': '👥',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Employee Group Health Insurance', '/static/images/grouped_icons/group_health.png'),
            ('Group Personal Accident', '/static/images/grouped_icons/group_personal_accident.png'),
            ('Group Term Life', '/static/images/grouped_icons/group_term_life.png'),
            ('COVID-19 Group Health Plan', '/static/images/grouped_icons/covid19_group_health.png'),
            ('Group Health Top-Up Plan', '/static/images/grouped_icons/group_health_topup_plan.png'),
            ('Group Gratuity Insurance', '/static/images/grouped_icons/group_gratuity_insurance.png'),
            ('Group Education Assistance', '/static/images/grouped_icons/group_education_assistance.png')
        ]
    },
    {
        'title': 'ENGINEERING',
        'icon': '🏗️',
        'grid_class': 'cat-grid-5col',
        'items': [
            ("Construction All Risk", '/static/images/grouped_icons/construction_all_risk.png'),
            ("Plant & Machinery Insurance", '/static/images/grouped_icons/plant_machinery_insurance.png'),
            ("Contractor's Plant & Machinery Insurance", '/static/images/grouped_icons/contractors_plant_machinery_insurance.png'),
            ("Electronic Equipment Insurance", '/static/images/grouped_icons/electronic_equipment_insurance.png'),
            ("Engineering Professional Indemnity", '/static/images/grouped_icons/engineering_professional_indemnity.png'),
            ("Machinery Breakdown Insurance", '/static/images/grouped_icons/machinery_breakdown_insurance.png'),
            ("Erection All Risk", '/static/images/grouped_icons/erection_all_risk.png')
        ]
    },
    {
        'title': 'MARINE & PROPERTY INSURANCE',
        'icon': '🚢',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Marine Insurance', '/static/images/grouped_icons/marine_insurance.png'),
            ('Home Insurance', '/static/images/grouped_icons/home_insurance.png'),
            ('Industrial All Risk Insurance', '/static/images/grouped_icons/industrial_all_risk_insurance.png'),
            ('Goods In Transit Insurance', '/static/images/grouped_icons/goods_in_transit_insurance.png'),
            ('Fire & Burglary', '/static/images/grouped_icons/fire_and_burglary.png'),
            ('Shop Owner Insurance', '/static/images/grouped_icons/shop_owner_open.png'),
            ('Office Package Policy', '/static/images/grouped_icons/office_policy_desk.png')
        ]
    },
    {
        'title': 'LIABILITY',
        'icon': '⚖️',
        'grid_class': 'cat-grid-7col',
        'items': [
            ('Professional Indemnity for Doctors', '/static/images/grouped_icons/professional_indemnity_doctors.png'),
            ('Professional Indemnity for Companies', '/static/images/grouped_icons/professional_indemnity_companies.png'),
            ('Workmen Compensation', '/static/images/grouped_icons/workmen_compensation.png'),
            ('General Liability', '/static/images/grouped_icons/general_liability.png'),
            ('Legal Liability Insurance', '/static/images/grouped_icons/legal_liability_insurance.png'),
            ('Cyber Risk Insurance', '/static/images/grouped_icons/cyber_risk_insurance.png'),
            ('Directors & Officers Liability', '/static/images/grouped_icons/directors_officers_liability.png')
        ]
    }
]

sec_html = ['\n  <!-- Categorized Products Section (Placed After Featured Financial Solutions) -->']
sec_html.append('  <section id="categorized-products" style="max-width:1350px; margin:50px auto 30px; padding:0 5%;">')

for cat in categories_data:
    title = cat['title']
    icon = cat['icon']
    grid_class = cat.get('grid_class', 'cat-grid-5col')
    sec_html.append(f'    <!-- Category: {title} -->')
    sec_html.append('    <div style="margin-bottom:40px;">')
    sec_html.append('      <div style="display:flex; align-items:center; gap:10px; margin-bottom:18px; border-bottom:2px solid #e2e8f0; padding-bottom:8px;">')
    sec_html.append(f'        <span style="font-size:1.3rem;">{icon}</span>')
    sec_html.append(f'        <h3 style="font-size:1.15rem; font-weight:800; color:#0f172a; letter-spacing:0.5px; margin:0;">{title}</h3>')
    sec_html.append('      </div>')
    
    sec_html.append(f'      <div class="{grid_class}">')
    for item_name, img_path in cat['items']:
        safe_name = item_name.replace("'", "\\'")
        escaped_title = item_name.replace("&", "&amp;")
        sec_html.append(f'        <div class="pb-card-7col" onclick="App.openEnquireModal(\'{safe_name}\')">')
        sec_html.append(f'          <img src="{img_path}?v=3" alt="{item_name}" class="pb-card-icon-img">')
        sec_html.append(f'          <div class="pb-card-7col-title">{escaped_title}</div>')
        sec_html.append('        </div>')
    sec_html.append('      </div>')
    sec_html.append('    </div>')

sec_html.append('  </section>\n')

category_section_block = '\n'.join(sec_html)

for html_path in html_paths:
    if not os.path.exists(html_path):
        continue
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<!-- Categorized Products Section \(Placed After Featured Financial Solutions\) -->\s*<section id="categorized-products".*?</section>'
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, category_section_block, content, flags=re.DOTALL)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'SUCCESS: Replaced categorized section in {html_path}')
    else:
        print(f'WARNING: Pattern not found in {html_path}')
