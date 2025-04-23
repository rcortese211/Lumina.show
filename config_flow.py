from homeassistant import config_entries
from . import DOMAIN

class LuminaShowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Lumina Show."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Lumina Show", data=user_input)

        return self.async_show_form(step_id="user")
