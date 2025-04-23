import { LitElement, html, css } from 'lit';

class PlaybackControls extends LitElement {
  static styles = css`
    /* Add styles for playback controls */
  `;

  render() {
    return html`
      <div class="playback-controls">
        <button @click="${this.play}">Play</button>
        <button @click="${this.pause}">Pause</button>
        <button @click="${this.stop}">Stop</button>
      </div>
    `;
  }

  play() {
    console.log('Play clicked');
  }

  pause() {
    console.log('Pause clicked');
  }

  stop() {
    console.log('Stop clicked');
  }
}

customElements.define('playback-controls', PlaybackControls);
