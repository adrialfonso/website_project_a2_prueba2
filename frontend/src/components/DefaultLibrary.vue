<template>
  <div id="leftcol" class="left-slider">
    <div class="library-content-wrap">
      <nav class="library-content">
        <header class="library-header btn">
          <div class="library-icon">
            <svg width="40" height="40" viewBox="0 0 47 28" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 19L20 19.3333L14 26V4.66667C14 3.95943 14.1806 3.28115 14.5021 2.78105C14.8236 2.28096
              15.2596 2 15.7143 2L18.3593 2C18.8139 2 19.2499 2.28095 19.5714 2.78105C19.8929 3.28115 20 4.29276 20 5V19Z"
                    fill="#535151" stroke="#535151" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M8 19L7.99998 19.3333L2 26V4.66667C2 3.95943 2.18061 3.28115 2.5021 2.78105C2.82359 2.28096 3.25962
              2 3.71428 2L6.35925 2C6.81391 2 7.24994 2.28095 7.57143 2.78105C7.89292 3.28115 8 4.29276 8 5V19Z"
                    fill="#535151" stroke="#535151" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M45 25L35.5 18.6111L26 25V4.55556C26 3.87778 26.286 3.22776 26.795 2.7485C27.304 2.26925 27.9944 2
              28.7143 2H42.2857C43.0056 2 43.696 2.26925 44.205 2.7485C44.714 3.22776 45 3.87778 45 4.55556V25Z"
                    fill="#535151" stroke="#535151" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="library-title-header">
            Your library
          </div>
        </header>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Library',
  data () {
    return {

    }
  }
}
</script>

<style scoped>
.left-slider {
  background: var(--box-background-color);
  overflow: auto;
  grid-area: left-slider;
  margin-right: calc(-1 * var(--panel-gap));
  border: 1px solid var(--box-border-color);
  border-radius: calc(var(--border-radius) *2);
  flex-direction: column;
  container-type: inline-size;
}

.library-content-wrap {
  display: flex;
  gap: var(--panel-gap);
  padding: var(--panel-gap);
}

.library-content {
  display: grid;
  gap: var(--panel-gap);
  grid-template-areas: 'nav-control'
                       'library-content';
  grid-template-rows: 1fr auto;
}

.library-header {
  padding-inline: calc(var(--panel-gap) *3);
  gap: var(--panel-gap);
  grid-area: nav-control;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  justify-items: center;
  border: 0;
}

.library-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.library-title-header {
  font-size: 1rem;
  color: var(--title-header-library);
  font-weight: bold;
  text-align: center;
}

@container (max-width: 12.5rem) {
  .library-title-header {
    display: none !important;
  }
}

@media (max-width: 42.375rem) {
  .left-slider {
    margin: var(--panel-gap);
  }
}
</style>
