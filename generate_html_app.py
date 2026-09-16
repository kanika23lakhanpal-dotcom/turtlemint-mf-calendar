# -*- coding: utf-8 -*-
import json

with open("curriculum_data.json", "r", encoding="utf-8") as f:
    raw_json = f.read()

html_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Turtlemint Mutual Fund Master Learning Calendar | Pro & Ninja</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            turtle: {
              primary: '#009F69',
              deep: '#007D64',
              mint: '#00d679',
              gold: '#FFB000',
              darkbg: '#0A120E',
              darkcard: '#111D17',
              darkborder: '#1B2E24'
            }
          },
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          }
        }
      }
    }
  </script>
  <style>
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0A120E; }
    ::-webkit-scrollbar-thumb { background: #007D64; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #009F69; }
    .gradient-header {
      background: linear-gradient(135deg, #0A120E 0%, #007D64 55%, #009F69 100%);
    }
    .brand-border-glow:hover {
      border-color: #00d679;
      box-shadow: 0 0 20px -5px rgba(0, 214, 121, 0.25);
    }
  </style>
</head>
<body class="bg-[#0A120E] text-slate-100 font-sans min-h-screen antialiased flex flex-col selection:bg-[#00d679] selection:text-[#0A120E]">

  <!-- Top Sticky Navigation Bar -->
  <header class="sticky top-0 z-50 bg-[#0A120E]/95 backdrop-blur-md border-b border-turtle-darkborder px-4 lg:px-8 py-3.5 transition-all">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3.5">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-turtle-mint via-turtle-primary to-turtle-deep flex items-center justify-center shadow-lg shadow-turtle-primary/30">
          <svg class="w-6 h-6 text-[#0A120E]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xl font-extrabold tracking-tight text-white">TURTLEMINT</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold tracking-widest uppercase bg-turtle-mint/20 text-turtle-mint border border-turtle-mint/40">PRO / NINJA</span>
          </div>
          <p class="text-xs text-slate-400 font-medium">Digital Partner Mutual Fund Master Learning Calendar</p>
        </div>
      </div>

      <!-- Live Search & Controls -->
      <div class="flex items-center gap-3 w-full md:w-auto">
        <div class="relative flex-1 md:w-80">
          <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input 
            id="searchInput" 
            type="text" 
            placeholder="Search SIP, NAV, Tax, KYC, Risk, FD..." 
            class="w-full bg-turtle-darkcard border border-turtle-darkborder rounded-xl pl-10 pr-4 py-2 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-turtle-mint focus:ring-1 focus:ring-turtle-mint transition"
          >
        </div>

        <button id="expandAllBtn" class="px-3.5 py-2 text-xs font-semibold bg-turtle-darkcard hover:bg-turtle-deep/40 text-slate-200 border border-turtle-darkborder rounded-xl transition flex items-center gap-1.5 whitespace-nowrap">
          <svg class="w-3.5 h-3.5 text-turtle-mint" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
          <span>Expand All</span>
        </button>

        <button onclick="window.print()" class="px-3.5 py-2 text-xs font-semibold bg-turtle-primary hover:bg-turtle-deep text-white rounded-xl shadow-md transition flex items-center gap-1.5 whitespace-nowrap">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path>
          </svg>
          <span>Print / PDF</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="gradient-header py-12 px-4 lg:px-8 border-b border-turtle-darkborder relative overflow-hidden">
    <div class="absolute -right-20 -top-20 w-96 h-96 bg-turtle-mint/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -left-20 -bottom-20 w-96 h-96 bg-turtle-gold/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto relative z-10">
      <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-turtle-deep/60 border border-turtle-mint/30 text-turtle-mint text-xs font-semibold uppercase tracking-wider mb-4">
        <span class="w-2 h-2 rounded-full bg-turtle-mint animate-pulse"></span>
        Zero-To-Hero Digital Partner Enablement Architecture
      </div>
      <h1 class="text-3xl md:text-5xl font-black text-white tracking-tight leading-tight max-w-4xl">
        Master Mutual Fund Learning Calendar
      </h1>
      <p class="mt-3 text-base md:text-lg text-slate-300 max-w-3xl font-normal leading-relaxed">
        Specially architected for <strong class="text-white">Turtlemint Digital Partners</strong>. Designed for learners with zero prior finance background. Built around real customer conversations, objection handling, and strict SEBI/AMFI compliance.
      </p>

      <!-- Key Metrics Row -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8">
        <div class="bg-[#0A120E]/75 backdrop-blur-md p-4 rounded-2xl border border-turtle-darkborder">
          <p class="text-xs uppercase tracking-wider text-slate-400 font-semibold">Total Levels</p>
          <p class="text-2xl md:text-3xl font-black text-turtle-mint mt-1">21 Levels</p>
          <p class="text-[11px] text-slate-500 mt-0.5">Level 0 to Level 20</p>
        </div>
        <div class="bg-[#0A120E]/75 backdrop-blur-md p-4 rounded-2xl border border-turtle-darkborder">
          <p class="text-xs uppercase tracking-wider text-slate-400 font-semibold">Thematic Modules</p>
          <p class="text-2xl md:text-3xl font-black text-white mt-1">31 Modules</p>
          <p class="text-[11px] text-slate-500 mt-0.5">Pedagogical Units</p>
        </div>
        <div class="bg-[#0A120E]/75 backdrop-blur-md p-4 rounded-2xl border border-turtle-darkborder">
          <p class="text-xs uppercase tracking-wider text-slate-400 font-semibold">Granular Lessons</p>
          <p class="text-2xl md:text-3xl font-black text-turtle-gold mt-1">73 Lessons</p>
          <p class="text-[11px] text-slate-500 mt-0.5">With Subtopics & Scripts</p>
        </div>
        <div class="bg-[#0A120E]/75 backdrop-blur-md p-4 rounded-2xl border border-turtle-darkborder">
          <p class="text-xs uppercase tracking-wider text-slate-400 font-semibold">Regulatory Standard</p>
          <p class="text-2xl md:text-3xl font-black text-white mt-1">Sept 2026</p>
          <p class="text-[11px] text-slate-500 mt-0.5">Post-Finance Act Ready</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Phase Filter Navigation -->
  <nav class="bg-turtle-darkcard border-b border-turtle-darkborder sticky top-[69px] z-40 px-4 lg:px-8 py-2.5 overflow-x-auto scrollbar-none">
    <div class="max-w-7xl mx-auto flex items-center gap-2 min-w-max" id="phaseFilterContainer">
      <button data-phase="all" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-bold transition bg-turtle-mint text-[#0A120E] shadow-sm">
        All Phases (21 Levels)
      </button>
      <button data-phase="Phase 1: Zero-to-One Foundations" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 1: Foundations (L0–L2)
      </button>
      <button data-phase="Phase 2: Product Anatomy & Everyday Operations" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 2: Products & Ops (L3–L5)
      </button>
      <button data-phase="Phase 3: The Diagnostic Eye — Risk, Returns & Factsheets" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 3: Risk & Returns (L6–L9)
      </button>
      <button data-phase="Phase 4: Goal Advisory, Tax & Costs" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 4: Goals, Tax & Cost (L10–L13)
      </button>
      <button data-phase="Phase 5: Field Mastery — Customer Discovery, Pitch & Compliance" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 5: Field Mastery (L14–L16)
      </button>
      <button data-phase="Phase 6: Advanced Capabilities, Real Personas & Certification" class="phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition">
        Phase 6: Advanced & Certification (L17–L20)
      </button>
    </div>
  </nav>

  <!-- Main Content Calendar Area -->
  <main class="max-w-7xl mx-auto px-4 lg:px-8 py-10 flex-1 w-full">
    <div id="calendarContainer" class="space-y-12">
      <!-- Injected via JavaScript -->
    </div>
  </main>

  <!-- Footer -->
  <footer class="bg-turtle-darkcard border-t border-turtle-darkborder py-8 px-4 lg:px-8 mt-12 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-300">Turtlemint Pro & Ninja</span>
        <span>•</span>
        <span>Mutual Fund Learning & Enablement Curriculum</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="inline-flex items-center gap-1.5 text-turtle-mint">
          <span class="w-1.5 h-1.5 rounded-full bg-turtle-mint"></span>
          SEBI / AMFI / NISM Compliant
        </span>
        <span>•</span>
        <span>Designed for Indian Digital Partners</span>
      </div>
    </div>
  </footer>

  <script>
    const curriculumData = __DATA_PLACEHOLDER__;
    let currentPhaseFilter = 'all';
    let currentSearchTerm = '';
    let allExpanded = false;

    const calendarContainer = document.getElementById('calendarContainer');
    const searchInput = document.getElementById('searchInput');
    const expandAllBtn = document.getElementById('expandAllBtn');
    const phaseFilterButtons = document.querySelectorAll('.phase-btn');

    function renderCalendar() {
      calendarContainer.innerHTML = '';
      let matchCount = 0;

      curriculumData.forEach((level) => {
        if (currentPhaseFilter !== 'all' && level.phase !== currentPhaseFilter) {
          return;
        }

        const matchingModules = [];

        level.modules.forEach(module => {
          const matchingLessons = module.lessons.filter(lesson => {
            if (!currentSearchTerm) return true;
            const searchHaystack = (
              level.level_title + ' ' +
              level.level_tagline + ' ' +
              module.module_title + ' ' +
              lesson.lesson_id + ' ' +
              lesson.title + ' ' +
              lesson.topic + ' ' +
              lesson.subtopics.join(' ') + ' ' +
              lesson.know + ' ' +
              lesson.understand + ' ' +
              lesson.do + ' ' +
              lesson.say + ' ' +
              lesson.never_claim
            ).toLowerCase();
            return searchHaystack.includes(currentSearchTerm.toLowerCase());
          });

          if (matchingLessons.length > 0) {
            matchingModules.push({
              ...module,
              lessons: matchingLessons
            });
          }
        });

        if (matchingModules.length === 0) return;
        matchCount++;

        const levelEl = document.createElement('section');
        levelEl.className = 'bg-turtle-darkcard border border-turtle-darkborder rounded-3xl overflow-hidden shadow-xl transition-all';
        
        let modulesHtml = '';
        matchingModules.forEach(mod => {
          let lessonsHtml = '';
          
          mod.lessons.forEach(lesson => {
            const subtopicsList = lesson.subtopics.map(sub => `
              <li class="flex items-start gap-2 text-xs text-slate-300">
                <span class="text-turtle-mint font-bold leading-none mt-1">▸</span>
                <span>${sub}</span>
              </li>
            `).join('');

            lessonsHtml += `
              <div class="lesson-card bg-[#0A120E]/80 border border-turtle-darkborder/80 brand-border-glow rounded-2xl p-5 transition-all">
                <div class="flex flex-wrap items-center justify-between gap-2.5 pb-3 border-b border-turtle-darkborder">
                  <div class="flex items-center gap-2.5">
                    <span class="font-mono text-xs font-bold px-2.5 py-1 rounded-lg bg-turtle-deep/40 text-turtle-mint border border-turtle-mint/30">
                      ${lesson.lesson_id}
                    </span>
                    <h5 class="text-base font-bold text-white tracking-tight">${lesson.title}</h5>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="text-[11px] font-medium px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                      ${lesson.duration}
                    </span>
                    <span class="text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-turtle-mint/10 text-turtle-mint border border-turtle-mint/20">
                      ${lesson.format}
                    </span>
                  </div>
                </div>

                <div class="mt-3">
                  <p class="text-xs font-semibold text-turtle-gold uppercase tracking-wider mb-1.5">Core Topic: ${lesson.topic}</p>
                  
                  <!-- Granular Subtopics List -->
                  <div class="bg-turtle-darkcard/90 rounded-xl p-3.5 border border-turtle-darkborder mt-2">
                    <p class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">Granular Subtopics Covered:</p>
                    <ul class="space-y-1.5">
                      ${subtopicsList}
                    </ul>
                  </div>

                  <!-- Collapsible 5-Pillar Competency Drawer -->
                  <div class="mt-4 pt-3 border-t border-turtle-darkborder">
                    <button class="toggle-drawer-btn text-xs font-semibold text-turtle-mint hover:text-white flex items-center gap-1.5 transition">
                      <span class="icon-toggle">▸</span>
                      <span>View DP Practice & Compliance Guide (Know, Understand, Do, Say, Never Claim)</span>
                    </button>
                    
                    <div class="drawer-content hidden mt-3.5 grid grid-cols-1 md:grid-cols-2 gap-3 pt-2 text-xs">
                      <div class="bg-emerald-950/20 border border-emerald-500/20 rounded-xl p-3">
                        <p class="font-bold text-emerald-400 mb-1 flex items-center gap-1">
                          <span>💡</span> WHAT DP MUST KNOW
                        </p>
                        <p class="text-slate-300">${lesson.know}</p>
                      </div>

                      <div class="bg-blue-950/20 border border-blue-500/20 rounded-xl p-3">
                        <p class="font-bold text-blue-400 mb-1 flex items-center gap-1">
                          <span>🧠</span> WHAT DP MUST UNDERSTAND
                        </p>
                        <p class="text-slate-300">${lesson.understand}</p>
                      </div>

                      <div class="bg-purple-950/20 border border-purple-500/20 rounded-xl p-3">
                        <p class="font-bold text-purple-400 mb-1 flex items-center gap-1">
                          <span>📱</span> WHAT DP MUST DO (TURTLEMINT APP)
                        </p>
                        <p class="text-slate-300">${lesson.do}</p>
                      </div>

                      <div class="bg-amber-950/20 border border-amber-500/20 rounded-xl p-3">
                        <p class="font-bold text-turtle-gold mb-1 flex items-center gap-1">
                          <span>🗣️</span> WHAT DP MUST SAY (HINGLISH SCRIPT)
                        </p>
                        <p class="text-slate-200 italic">${lesson.say}</p>
                      </div>

                      <div class="bg-rose-950/20 border border-rose-500/30 rounded-xl p-3 md:col-span-2">
                        <p class="font-bold text-rose-400 mb-1 flex items-center gap-1">
                          <span>⛔</span> WHAT DP MUST NEVER CLAIM (COMPLIANCE RED LINE)
                        </p>
                        <p class="text-rose-200/90 font-medium">${lesson.never_claim}</p>
                      </div>
                    </div>
                  </div>

                </div>
              </div>
            `;
          });

          modulesHtml += `
            <div class="space-y-4">
              <div class="flex items-center gap-3">
                <span class="text-xs font-black px-2.5 py-1 rounded bg-turtle-deep text-white">
                  ${mod.module_id}
                </span>
                <h4 class="text-lg font-bold text-slate-100 tracking-tight">${mod.module_title}</h4>
              </div>
              <div class="grid grid-cols-1 gap-4 pl-0 md:pl-4 border-l-0 md:border-l-2 md:border-turtle-darkborder">
                ${lessonsHtml}
              </div>
            </div>
          `;
        });

        levelEl.innerHTML = `
          <!-- Level Header -->
          <div class="p-6 md:p-8 bg-gradient-to-r from-turtle-darkcard via-turtle-deep/20 to-turtle-darkcard border-b border-turtle-darkborder flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center gap-3 mb-2">
                <span class="px-3 py-1 rounded-lg text-xs font-black tracking-wider uppercase bg-turtle-mint text-[#0A120E]">
                  LEVEL ${level.level_num}
                </span>
                <span class="text-xs font-semibold text-slate-400">${level.phase}</span>
              </div>
              <h3 class="text-2xl md:text-3xl font-black text-white tracking-tight">${level.level_title}</h3>
              <p class="text-sm text-slate-300 mt-1 font-medium">${level.level_tagline}</p>
            </div>
            <div class="text-right flex md:flex-col items-center md:items-end justify-between">
              <span class="text-xs text-slate-400 font-medium">Included Modules</span>
              <span class="text-lg font-bold text-turtle-gold">${matchingModules.length} Modules</span>
            </div>
          </div>

          <!-- Level Body -->
          <div class="p-6 md:p-8 space-y-8">
            ${modulesHtml}
          </div>
        `;

        calendarContainer.appendChild(levelEl);
      });

      if (matchCount === 0) {
        calendarContainer.innerHTML = `
          <div class="bg-turtle-darkcard border border-turtle-darkborder rounded-3xl p-12 text-center max-w-lg mx-auto">
            <svg class="w-16 h-16 text-slate-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <h3 class="text-lg font-bold text-white">No Matching Lessons Found</h3>
            <p class="text-sm text-slate-400 mt-2">Try adjusting your search keywords or switch to 'All Phases'.</p>
            <button onclick="clearSearch()" class="mt-5 px-4 py-2 text-xs font-semibold bg-turtle-mint text-[#0A120E] rounded-xl">
              Clear Search Filter
            </button>
          </div>
        `;
      }

      // Attach Drawer Listeners
      document.querySelectorAll('.toggle-drawer-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const drawer = btn.nextElementSibling;
          const icon = btn.querySelector('.icon-toggle');
          if (drawer.classList.contains('hidden')) {
            drawer.classList.remove('hidden');
            icon.textContent = '▼';
          } else {
            drawer.classList.add('hidden');
            icon.textContent = '▸';
          }
        });
      });
    }

    function clearSearch() {
      searchInput.value = '';
      currentSearchTerm = '';
      renderCalendar();
    }

    searchInput.addEventListener('input', (e) => {
      currentSearchTerm = e.target.value.trim();
      renderCalendar();
    });

    phaseFilterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        phaseFilterButtons.forEach(b => {
          b.className = 'phase-btn px-4 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-turtle-deep/30 transition';
        });
        btn.className = 'phase-btn px-4 py-1.5 rounded-xl text-xs font-bold transition bg-turtle-mint text-[#0A120E] shadow-sm';
        currentPhaseFilter = btn.getAttribute('data-phase');
        renderCalendar();
      });
    });

    expandAllBtn.addEventListener('click', () => {
      allExpanded = !allExpanded;
      document.querySelectorAll('.drawer-content').forEach(d => {
        if (allExpanded) {
          d.classList.remove('hidden');
        } else {
          d.classList.add('hidden');
        }
      });
      document.querySelectorAll('.icon-toggle').forEach(i => {
        i.textContent = allExpanded ? '▼' : '▸';
      });
      expandAllBtn.querySelector('span').textContent = allExpanded ? 'Collapse All' : 'Expand All';
    });

    // Initial render
    renderCalendar();
  </script>
</body>
</html>
"""

final_html = html_template.replace("__DATA_PLACEHOLDER__", raw_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("index.html generated successfully with size:", len(final_html), "bytes")
