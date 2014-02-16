---
title: Talon Speed Controller
layout: default
categories:  [ hardware, public]
---
[User manual](Talon_User_Manual_1_3.pdf) - [source](http://www.crosstheroadelectronics.com/Talon.html)

## LED Blink Codes

<table class="table table-bordered table-striped">
	<thead>
		<tr>
			<th>LED</th>
			<th>Meaning</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Solid RED</td>
			<td>Full power - reverse</td>
		</tr>
		<tr>
			<td>Blinking RED</td>
			<td>Partial power - reverse (blink rate corresponds to percentage power)</td>
		</tr>
		<tr>
			<td>Solid GREEN</td>
			<td>Full power - forward</td>
		</tr>
		<tr>
			<td>Blinking GREEN</td>
			<td>Partial power - forward (blink rate corresponds to percentage power)</td>
		</tr>
		<tr>
			<td>Solid ORANGE</td>
			<td>Idle (within 4% of zero power)</td>
		</tr>
		<tr>
			<td>Blinking ORANGE</td>
			<td>Disabled</td>
		</tr>
		<tr>
			<td>Blinking RED/GREEN</td>
			<td>Ready for calibration.  After calibration, green flashes mean success, red flashed mean failure</td>
		</tr>
	</tbody>
</table>