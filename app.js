/**
 * PAYTM INNOVATION CHALLENGE 2026 — REAL AUDITED VOC DATASET VISUALIZATION
 * Dataset: Paytm UPI Growth Challenge 2026 — Raw Short VOC Responses.xlsx
 * Total Sample Size: N = 111 Authentic Respondents
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. EXACT REAL DATASET SPECIFICATION (N = 111)
  const REAL_DATA = {
    totalRespondents: 111,
    citiesCount: 20,
    statesCount: 13,
    tier3RuralCount: 72,
    tier3RuralPct: 64.86,
    urbanMetroCount: 39,
    urbanMetroPct: 35.14,
    
    paytm90dActiveCount: 71,
    paytm90dActivePct: 63.96,
    paytmPrimaryCount: 17,
    paytmPrimaryPct: 15.32,
    highFreqCount: 46,
    highFreqPct: 41.44,

    // Real City-level distribution with intelligent non-colliding offsets
    cities: [
      { name: "Sitapur", count: 39, coords: [80.6780, 27.5684], state: "Uttar Pradesh", type: "Tier-3 Town / Campus Cluster", dx: 35, dy: -6, showLabel: true, isCallout: true },
      { name: "Bhopal", count: 10, coords: [77.4126, 23.2599], state: "Madhya Pradesh", type: "Tier-2 / University Hub", dx: -60, dy: -6, showLabel: true, isCallout: true },
      { name: "Lucknow", count: 8, coords: [80.9462, 26.8467], state: "Uttar Pradesh", type: "Tier-2 Capital / Commercial", dx: 30, dy: 16, showLabel: true, isCallout: true },
      { name: "Lakhimpur Kheri", count: 8, coords: [80.7777, 27.9458], state: "Uttar Pradesh", type: "Tier-3 Town / Agri-Center", dx: 30, dy: -24, showLabel: true, isCallout: true },
      { name: "Ballia", count: 4, coords: [84.1497, 25.7581], state: "Uttar Pradesh", type: "East UP Town", dx: 25, dy: 4, showLabel: true, isCallout: false },
      { name: "Shahjahanpur", count: 3, coords: [79.9122, 27.8805], state: "Uttar Pradesh", type: "Tier-3 Town", dx: -80, dy: -14, showLabel: true, isCallout: true },
      { name: "Hardoi", count: 3, coords: [80.1264, 27.3989], state: "Uttar Pradesh", type: "Tier-3 Town", dx: -65, dy: 10, showLabel: true, isCallout: true },
      { name: "Biswan", count: 3, coords: [81.0028, 27.4939], state: "Uttar Pradesh", type: "Rural / Semi-Urban", dx: 25, dy: 2, showLabel: false, isCallout: false },
      { name: "Sehore", count: 2, coords: [77.0847, 23.2032], state: "Madhya Pradesh", type: "Semi-Urban Town", dx: -60, dy: 16, showLabel: true, isCallout: true },
      { name: "Bengaluru", count: 2, coords: [77.5946, 12.9716], state: "Karnataka", type: "Metro Tech Hub", dx: 22, dy: 4, showLabel: true, isCallout: false },
      { name: "Agra", count: 2, coords: [78.0081, 27.1767], state: "Uttar Pradesh", type: "Tier-2 Commercial", dx: -50, dy: 4, showLabel: true, isCallout: false },
      { name: "Delhi (NCR)", count: 2, coords: [77.1025, 28.7041], state: "Delhi (NCR)", type: "National Capital Region", dx: 20, dy: -8, showLabel: true, isCallout: false },
      { name: "Gurgaon", count: 2, coords: [77.0266, 28.4595], state: "Haryana", type: "Corporate Tech Hub", dx: -60, dy: 8, showLabel: false, isCallout: false },
      { name: "Noida", count: 1, coords: [77.3910, 28.5355], state: "Uttar Pradesh", type: "Urban / NCR Hub", dx: 18, dy: 2, showLabel: false, isCallout: false },
      { name: "Dehradun", count: 1, coords: [78.0322, 30.3165], state: "Uttarakhand", type: "State Capital / Education", dx: 20, dy: -4, showLabel: true, isCallout: false },
      { name: "Panipat", count: 1, coords: [76.9635, 29.3909], state: "Haryana", type: "Industrial Town", dx: -55, dy: -4, showLabel: false, isCallout: false },
      { name: "Shimla", count: 1, coords: [77.1734, 31.1048], state: "Himachal Pradesh", type: "Hill Capital / Tourism", dx: 18, dy: -6, showLabel: true, isCallout: false },
      { name: "Surat", count: 1, coords: [72.8311, 21.1702], state: "Gujarat", type: "Tier-2 Commercial Hub", dx: -50, dy: 4, showLabel: true, isCallout: false },
      { name: "Pune", count: 1, coords: [73.8567, 18.5204], state: "Maharashtra", type: "Education & IT Hub", dx: -45, dy: 8, showLabel: true, isCallout: false },
      { name: "Sangli", count: 1, coords: [74.5815, 16.8524], state: "Maharashtra", type: "Commercial Town", dx: -45, dy: 16, showLabel: false, isCallout: false },
      { name: "Bhubaneswar", count: 1, coords: [85.8245, 20.2961], state: "Odisha", type: "East Capital Hub", dx: 20, dy: 4, showLabel: true, isCallout: false },
      { name: "Jamshedpur", count: 1, coords: [86.2029, 22.8046], state: "Jharkhand", type: "Industrial City", dx: 20, dy: -4, showLabel: true, isCallout: false },
      { name: "Indore", count: 1, coords: [75.8577, 22.7196], state: "Madhya Pradesh", type: "Commercial Capital", dx: -45, dy: -10, showLabel: false, isCallout: false }
    ],

    // Real State distribution (All 13 States/UTs from dataset)
    states: [
      { state: "Uttar Pradesh", count: 81, pct: 72.97 },
      { state: "Madhya Pradesh", count: 13, pct: 11.71 },
      { state: "Haryana", count: 4, pct: 3.60 },
      { state: "Karnataka", count: 2, pct: 1.80 },
      { state: "Maharashtra", count: 2, pct: 1.80 },
      { state: "Delhi (NCR)", count: 2, pct: 1.80 },
      { state: "Uttarakhand", count: 1, pct: 0.90 },
      { state: "Himachal Pradesh", count: 1, pct: 0.90 },
      { state: "Gujarat", count: 1, pct: 0.90 },
      { state: "Odisha", count: 1, pct: 0.90 },
      { state: "Rajasthan", count: 1, pct: 0.90 },
      { state: "Jharkhand", count: 1, pct: 0.90 },
      { state: "Other (Overseas / Unmapped)", count: 1, pct: 0.90 }
    ],

    // Real Top Cities from audited dataset
    topCities: [
      { name: "Sitapur", count: 39, pct: 35.14 },
      { name: "Bhopal", count: 10, pct: 9.01 },
      { name: "Lucknow", count: 8, pct: 7.21 },
      { name: "Lakhimpur Kheri", count: 8, pct: 7.21 },
      { name: "Ballia", count: 4, pct: 3.60 },
      { name: "Shahjahanpur", count: 3, pct: 2.70 },
      { name: "Biswan", count: 3, pct: 2.70 },
      { name: "Hardoi", count: 3, pct: 2.70 }
    ],

    // Real Profile Distribution (Question 1)
    profiles: [
      { profile: "College student", count: 69, pct: 62.16 },
      { profile: "Working professional", count: 23, pct: 20.72 },
      { profile: "Other (Homemaker / Job Seeker)", count: 10, pct: 9.01 },
      { profile: "Self-employed / freelancer", count: 9, pct: 8.11 }
    ]
  };

  const tooltip = document.getElementById('dashboard-tooltip');

  function showTooltip(html, event) {
    tooltip.innerHTML = html;
    tooltip.style.opacity = '1';
    positionTooltip(event);
  }

  function positionTooltip(event) {
    const pad = 14;
    let x = event.clientX + pad;
    let y = event.clientY + pad;
    const tipRect = tooltip.getBoundingClientRect();
    if (x + tipRect.width > window.innerWidth - 20) {
      x = event.clientX - tipRect.width - pad;
    }
    if (y + tipRect.height > window.innerHeight - 20) {
      y = event.clientY - tipRect.height - pad;
    }
    tooltip.style.left = `${x}px`;
    tooltip.style.top = `${y}px`;
  }

  function hideTooltip() {
    tooltip.style.opacity = '0';
  }

  // ------------------------------------------------------------------------
  // 1. RENDER INDIA MAP (STATE INTENSITY CHOROPLETH + COLLISION-FREE MARKERS)
  // ------------------------------------------------------------------------
  function renderIndiaMap() {
    const container = document.getElementById('india-map-container');
    container.innerHTML = '';

    const width = container.clientWidth || 680;
    const height = container.clientHeight || 640;

    const svg = d3.select(container)
      .append('svg')
      .attr('width', '100%')
      .attr('height', '100%')
      .attr('viewBox', `0 0 ${width} ${height}`)
      .attr('preserveAspectRatio', 'xMidYMid meet');

    const g = svg.append('g').attr('class', 'map-root-group');

    // Projection optimized for India
    const projection = d3.geoMercator()
      .center([81.5, 23.5])
      .scale(width * 1.55)
      .translate([width / 2, height / 2]);

    const pathGenerator = d3.geoPath().projection(projection);

    const zoom = d3.zoom()
      .scaleExtent([0.8, 6])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      });

    svg.call(zoom);

    document.getElementById('btn-reset-zoom').onclick = () => {
      svg.transition().duration(600).call(zoom.transform, d3.zoomIdentity);
    };

    // State Color Intensity Shading Helper
    function getStateFill(stateName) {
      const s = stateName.toLowerCase();
      if (s.includes('uttar pradesh')) return '#BFDBFE'; // Prominent UP (81 respondents)
      if (s.includes('madhya pradesh')) return '#DBEAFE'; // MP (13 respondents)
      if (s.includes('haryana')) return '#E0F2FE';
      if (s.includes('karnataka') || s.includes('maharashtra') || s.includes('delhi') || s.includes('uttarakhand') || s.includes('himachal') || s.includes('gujarat') || s.includes('orissa') || s.includes('odisha') || s.includes('rajasthan') || s.includes('jharkhand')) {
        return '#F0F7FF'; // Active state tint
      }
      return '#F8FAFC'; // Inactive state neutral
    }

    function getStateStroke(stateName) {
      const s = stateName.toLowerCase();
      if (s.includes('uttar pradesh')) return '#3B82F6';
      if (s.includes('madhya pradesh')) return '#60A5FA';
      if (s.includes('haryana') || s.includes('karnataka') || s.includes('maharashtra') || s.includes('delhi')) {
        return '#93C5FD';
      }
      return '#CBD5E1';
    }

    if (typeof INDIA_GEOJSON !== 'undefined' && INDIA_GEOJSON.features) {
      g.append('g')
        .attr('class', 'states-layer')
        .selectAll('path')
        .data(INDIA_GEOJSON.features)
        .enter()
        .append('path')
        .attr('d', pathGenerator)
        .attr('class', 'state-path')
        .style('fill', d => {
          const sName = (d.properties && d.properties.name) ? d.properties.name : '';
          return getStateFill(sName);
        })
        .style('stroke', d => {
          const sName = (d.properties && d.properties.name) ? d.properties.name : '';
          return getStateStroke(sName);
        })
        .style('stroke-width', d => {
          const sName = (d.properties && d.properties.name) ? d.properties.name.toLowerCase() : '';
          return sName.includes('uttar pradesh') ? '1.5px' : '0.8px';
        })
        .on('mouseenter', (event, d) => {
          const sName = (d.properties && d.properties.name) || 'State / UT';
          const match = REAL_DATA.states.find(s => sName.toLowerCase().includes(s.state.toLowerCase()) || s.state.toLowerCase().includes(sName.toLowerCase()));
          const count = match ? match.count : 0;
          const pct = match ? match.pct.toFixed(1) + '%' : '0.0%';
          
          showTooltip(`
            <div class="tooltip-title">${sName}</div>
            <div class="tooltip-row"><span class="tooltip-label">VOC Responses:</span><span class="tooltip-val">${count}</span></div>
            <div class="tooltip-row"><span class="tooltip-label">% of Total Sample:</span><span class="tooltip-val">${pct}</span></div>
          `, event);
        })
        .on('mousemove', positionTooltip)
        .on('mouseleave', hideTooltip);
    }

    function getRadius(count) {
      if (count >= 30) return 18; // Sitapur
      if (count >= 8) return 12;  // Bhopal, Lucknow, Lakhimpur
      if (count >= 3) return 8;   // Ballia, Shahjahanpur, Hardoi, Biswan
      if (count >= 2) return 6;
      return 4.5;
    }

    function getColor(count) {
      if (count >= 30) return '#002970'; // Deep Navy
      if (count >= 8) return '#0052CC';  // Royal Blue
      if (count >= 3) return '#00BAF2';  // Paytm Cyan
      if (count >= 2) return '#38BDF8';  // Light Blue
      return '#93C5FD';                  // Subtle Sky Blue
    }

    const cityLayer = g.append('g').attr('class', 'cities-layer');

    const cityGroups = cityLayer.selectAll('.city-bubble')
      .data(REAL_DATA.cities)
      .enter()
      .append('g')
      .attr('class', 'city-bubble')
      .attr('transform', d => {
        const p = projection(d.coords);
        return p ? `translate(${p[0]}, ${p[1]})` : 'translate(-100,-100)';
      });

    // Outer glow ring for top clusters
    cityGroups.filter(d => d.count >= 8)
      .append('circle')
      .attr('r', d => getRadius(d.count) + 5)
      .attr('class', 'city-bubble-glow');

    // Main circle
    cityGroups.append('circle')
      .attr('r', d => getRadius(d.count))
      .attr('fill', d => getColor(d.count))
      .attr('class', 'city-bubble-circle');

    // Center white dot for dense hubs
    cityGroups.filter(d => d.count >= 8)
      .append('circle')
      .attr('r', 3)
      .attr('fill', '#FFFFFF');

    // Leader Callout Lines Layer
    const calloutLayer = g.append('g').attr('class', 'callout-layer');
    REAL_DATA.cities.filter(d => d.showLabel && d.isCallout).forEach(d => {
      const p = projection(d.coords);
      if (p) {
        calloutLayer.append('line')
          .attr('x1', p[0])
          .attr('y1', p[1])
          .attr('x2', p[0] + (d.dx * 0.75))
          .attr('y2', p[1] + (d.dy * 0.75))
          .attr('class', 'callout-line');
      }
    });

    // City Text Labels Layer (Rendered only for clean, non-overlapping cities)
    const labelLayer = g.append('g').attr('class', 'city-labels-layer');
    const labeledCities = REAL_DATA.cities.filter(d => d.showLabel);

    const labelGroups = labelLayer.selectAll('.city-label-group')
      .data(labeledCities)
      .enter()
      .append('g')
      .attr('class', 'city-label-group')
      .attr('transform', d => {
        const p = projection(d.coords);
        const ox = d.dx || 14;
        const oy = d.dy || 0;
        return p ? `translate(${p[0] + ox}, ${p[1] + oy})` : 'translate(-100,-100)';
      });

    labelGroups.append('text')
      .attr('class', 'city-text-bg')
      .attr('text-anchor', d => (d.dx < 0 ? 'end' : 'start'))
      .attr('dy', '0.35em')
      .text(d => `${d.name} (${d.count})`);

    labelGroups.append('text')
      .attr('class', 'city-text')
      .attr('text-anchor', d => (d.dx < 0 ? 'end' : 'start'))
      .attr('dy', '0.35em')
      .text(d => `${d.name} `)
      .append('tspan')
      .attr('class', 'city-count-badge')
      .text(d => `(${d.count})`);

    // Hover Interaction
    cityGroups
      .on('mouseenter', (event, d) => {
        const pct = ((d.count / REAL_DATA.totalRespondents) * 100).toFixed(1);
        showTooltip(`
          <div class="tooltip-title">${d.name}</div>
          <div class="tooltip-row"><span class="tooltip-label">State / UT:</span><span class="tooltip-val">${d.state}</span></div>
          <div class="tooltip-row"><span class="tooltip-label">VOC Responses:</span><span class="tooltip-val">${d.count} (${pct}%)</span></div>
          <div class="tooltip-row"><span class="tooltip-label">Settlement Type:</span><span class="tooltip-val">${d.type}</span></div>
        `, event);
      })
      .on('mousemove', positionTooltip)
      .on('mouseleave', hideTooltip);
  }

  // ------------------------------------------------------------------------
  // 2. RENDER REAL STATE-WISE HORIZONTAL BARS (ALL 13 STATES)
  // ------------------------------------------------------------------------
  function renderStateChart() {
    const container = document.getElementById('state-chart-container');
    const maxVal = REAL_DATA.states[0].count; // UP (81)

    let html = '';
    REAL_DATA.states.forEach(item => {
      const widthPct = Math.max(((item.count / maxVal) * 100), 2.5).toFixed(1);
      html += `
        <div class="bar-row-item" data-state="${item.state}" data-count="${item.count}">
          <div class="bar-label-text" title="${item.state}">${item.state}</div>
          <div class="bar-track">
            <div class="bar-fill bar-fill-state" style="width: ${widthPct}%;"></div>
          </div>
          <div class="bar-val-badge">
            <span>${item.count}</span>
            <span class="bar-pct">(${item.pct.toFixed(1)}%)</span>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;

    container.querySelectorAll('.bar-row-item').forEach(el => {
      el.addEventListener('mouseenter', (e) => {
        const state = el.getAttribute('data-state');
        const count = el.getAttribute('data-count');
        const pct = ((count / REAL_DATA.totalRespondents) * 100).toFixed(1);
        showTooltip(`
          <div class="tooltip-title">${state}</div>
          <div class="tooltip-row"><span class="tooltip-label">Respondents:</span><span class="tooltip-val">${count}</span></div>
          <div class="tooltip-row"><span class="tooltip-label">% of Total Sample:</span><span class="tooltip-val">${pct}%</span></div>
        `, e);
      });
      el.addEventListener('mousemove', positionTooltip);
      el.addEventListener('mouseleave', hideTooltip);
    });
  }

  // ------------------------------------------------------------------------
  // 3. RENDER TIER-3/RURAL VS URBAN METROS DONUT CHART
  // ------------------------------------------------------------------------
  function renderUrbanRuralDonut() {
    const container = document.getElementById('urban-rural-donut');
    container.innerHTML = '';

    const width = 180;
    const height = 180;
    const radius = Math.min(width, height) / 2;
    const innerRadius = radius * 0.65;

    const svg = d3.select(container)
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr('transform', `translate(${width / 2}, ${height / 2})`);

    const donutData = [
      { label: "Tier-3 & Rural Towns", value: REAL_DATA.tier3RuralPct, count: REAL_DATA.tier3RuralCount, color: "#0D9488" },
      { label: "Urban Metros & Capitals", value: REAL_DATA.urbanMetroPct, count: REAL_DATA.urbanMetroCount, color: "#0052CC" }
    ];

    const pie = d3.pie().value(d => d.value).sort(null);
    const arc = d3.arc().innerRadius(innerRadius).outerRadius(radius - 6).cornerRadius(4).padAngle(0.04);
    const arcHover = d3.arc().innerRadius(innerRadius).outerRadius(radius - 2).cornerRadius(4).padAngle(0.04);

    svg.selectAll('path')
      .data(pie(donutData))
      .enter()
      .append('path')
      .attr('d', arc)
      .attr('fill', d => d.data.color)
      .style('cursor', 'pointer')
      .on('mouseenter', function(event, d) {
        d3.select(this).transition().duration(150).attr('d', arcHover);
        showTooltip(`
          <div class="tooltip-title">${d.data.label}</div>
          <div class="tooltip-row"><span class="tooltip-label">Respondents:</span><span class="tooltip-val">${d.data.count} of 111</span></div>
          <div class="tooltip-row"><span class="tooltip-label">Share:</span><span class="tooltip-val">${d.data.value.toFixed(1)}%</span></div>
        `, event);
      })
      .on('mousemove', positionTooltip)
      .on('mouseleave', function() {
        d3.select(this).transition().duration(150).attr('d', arc);
        hideTooltip();
      });

    const centerGroup = svg.append('g').attr('class', 'donut-center-text-group');
    centerGroup.append('text').attr('class', 'donut-center-num').attr('dy', '-0.05em').text('111');
    centerGroup.append('text').attr('class', 'donut-center-label').attr('dy', '1.35em').text('Respondents');

    const legendContainer = d3.select('#urban-rural-donut').append('div').attr('class', 'donut-legend');
    legendContainer.html(`
      <div class="donut-legend-item"><span class="legend-dot dot-rural"></span><span>Tier-3/Rural ${REAL_DATA.tier3RuralPct.toFixed(0)}%</span></div>
      <div class="donut-legend-item"><span class="legend-dot dot-urban"></span><span>Urban ${REAL_DATA.urbanMetroPct.toFixed(0)}%</span></div>
    `);
  }

  // ------------------------------------------------------------------------
  // 4. RENDER TOP CITIES VERTICAL BARS (AUDITED REAL CITIES)
  // ------------------------------------------------------------------------
  function renderTopCitiesChart() {
    const container = document.getElementById('top-cities-chart-container');
    const maxVal = REAL_DATA.topCities[0].count; // Sitapur (39)

    let html = '<div class="vertical-chart-body">';
    REAL_DATA.topCities.forEach(item => {
      const heightPct = Math.max(((item.count / maxVal) * 100), 5).toFixed(1);

      html += `
        <div class="v-bar-col" data-city="${item.name}" data-count="${item.count}" data-share="${item.pct.toFixed(1)}">
          <div class="v-bar-val">${item.count}</div>
          <div class="v-bar-track">
            <div class="v-bar-fill" style="height: ${heightPct}%;"></div>
          </div>
          <div class="v-bar-label" title="${item.name}">${item.name}</div>
        </div>
      `;
    });
    html += '</div>';
    container.innerHTML = html;

    container.querySelectorAll('.v-bar-col').forEach(col => {
      col.addEventListener('mouseenter', (e) => {
        const city = col.getAttribute('data-city');
        const count = col.getAttribute('data-count');
        const share = col.getAttribute('data-share');
        showTooltip(`
          <div class="tooltip-title">${city}</div>
          <div class="tooltip-row"><span class="tooltip-label">Respondents:</span><span class="tooltip-val">${count}</span></div>
          <div class="tooltip-row"><span class="tooltip-label">% of Total Sample:</span><span class="tooltip-val">${share}%</span></div>
        `, e);
      });
      col.addEventListener('mousemove', positionTooltip);
      col.addEventListener('mouseleave', hideTooltip);
    });
  }

  // ------------------------------------------------------------------------
  // 5. RENDER PROFESSION BARS (QUESTION 1 AUDITED REAL PROFILES)
  // ------------------------------------------------------------------------
  function renderProfessionChart() {
    const container = document.getElementById('profession-chart-container');
    const maxVal = REAL_DATA.profiles[0].count; // College student (69)

    let html = '';
    REAL_DATA.profiles.forEach(item => {
      const widthPct = Math.max(((item.count / maxVal) * 100), 4).toFixed(1);
      html += `
        <div class="bar-row-item" data-prof="${item.profile}" data-count="${item.count}">
          <div class="bar-label-text" title="${item.profile}">${item.profile}</div>
          <div class="bar-track">
            <div class="bar-fill bar-fill-prof" style="width: ${widthPct}%;"></div>
          </div>
          <div class="bar-val-badge">
            <span>${item.count}</span>
            <span class="bar-pct">(${item.pct.toFixed(1)}%)</span>
          </div>
        </div>
      `;
    });
    container.innerHTML = html;

    container.querySelectorAll('.bar-row-item').forEach(el => {
      el.addEventListener('mouseenter', (e) => {
        const prof = el.getAttribute('data-prof');
        const count = el.getAttribute('data-count');
        const pct = ((count / REAL_DATA.totalRespondents) * 100).toFixed(1);
        showTooltip(`
          <div class="tooltip-title">${prof}</div>
          <div class="tooltip-row"><span class="tooltip-label">Respondents:</span><span class="tooltip-val">${count}</span></div>
          <div class="tooltip-row"><span class="tooltip-label">% of Total Sample:</span><span class="tooltip-val">${pct}%</span></div>
        `, e);
      });
      el.addEventListener('mousemove', positionTooltip);
      el.addEventListener('mouseleave', hideTooltip);
    });
  }

  // ------------------------------------------------------------------------
  // 6. FILTER CHIPS LOGIC FOR REAL DATASET
  // ------------------------------------------------------------------------
  const filterChips = document.querySelectorAll('.filter-chip');
  const activeFilterLabel = document.getElementById('active-filter-label');

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      const filterType = chip.getAttribute('data-filter');
      
      if (activeFilterLabel) {
        activeFilterLabel.textContent = chip.textContent;
      }

      d3.selectAll('.city-bubble').transition().duration(300)
        .style('opacity', function(d) {
          if (filterType === 'all') return 1;
          if (filterType === 'prof-student') return (['Sitapur', 'Bhopal', 'Lucknow', 'Lakhimpur Kheri', 'Dehradun', 'Ballia'].includes(d.name)) ? 1 : 0.2;
          if (filterType === 'prof-pro') return (['Lucknow', 'Bhopal', 'Delhi (NCR)', 'Bengaluru', 'Noida', 'Gurgaon', 'Surat'].includes(d.name)) ? 1 : 0.2;
          if (filterType === 'seg-tier3') return (d.type.includes('Tier-3') || d.type.includes('Rural') || d.type.includes('Semi-Urban') || d.type.includes('Town')) ? 1 : 0.2;
          if (filterType === 'seg-urban') return (!d.type.includes('Rural') && !d.type.includes('Tier-3') && !d.type.includes('Town')) ? 1 : 0.2;
          return 1;
        });
    });
  });

  // INITIALIZE ALL
  renderIndiaMap();
  renderStateChart();
  renderUrbanRuralDonut();
  renderTopCitiesChart();
  renderProfessionChart();

  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      renderIndiaMap();
    }, 250);
  });
});
