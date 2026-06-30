# 1. Állítsunk le mindent teljesen
systemctl --user stop pipewire.service pipewire.socket pipewire-pulse.service pipewire-pulse.socket wireplumber.service

# 2. Töröljük a "start-limit-hit" hibaállapotot (ez reseteli a számlálót)
systemctl --user reset-failed pipewire.service pipewire.socket pipewire-pulse.service pipewire-pulse.socket wireplumber.service

# 3. Indítsuk el először a socketeket és a főbb szolgáltatásokat tiszta lappal
systemctl --user start pipewire.socket pipewire-pulse.socket
systemctl --user start pipewire.service pipewire-pulse.service wireplumber.service
