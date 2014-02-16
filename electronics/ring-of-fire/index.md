---
layout: default
title: Livewire Ring Of Fire RGB LED Ring
categories: [ hardware, public]
tags: [ camera, vision]
---

From [LiveWireRobotics.com](LiveWireRobotics)

Programmable LED ring that can change colors on the fly via I2C.

I2C address: 0x26

<table class="table table-bordered table-striped">
	<thead>
		<tr>
			<th>Value</th>
			<th>Color</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0x00</td>
			<td>All lights off</td>
		</tr>
		<tr>
			<td>0x01</td>
			<td>Red</td>
		</tr>
		<tr>
			<td>0x02</td>
			<td>Blue</td>
		</tr>
		<tr>
			<td>0x03</td>
			<td>Green</td>
		</tr>
		<tr>
			<td>0x04</td>
			<td>Yellow</td>
		</tr>
		<tr>
			<td>0x05</td>
			<td>Purple</td>
		</tr>
		<tr>
			<td>0x06</td>
			<td>Aqua</td>
		</tr>
		<tr>
			<td>0x07</td>
			<td>White</td>
		</tr>
		<tr>
			<td>0x08</td>
			<td>Infrared</td>
		</tr>
		<tr>
			<td>0x09</td>
			<td>Red blinking</td>
		</tr>
		<tr>
			<td>0x0a</td>
			<td>Red and yellow</td>
		</tr>
	</tbody>
</table>

One thing to note is that the I2C pins do **NOT** match the pin order on the [FRC Digital Sidecar](../frc-digital-sidecar/index.html).

<table class="table table-bordered table-striped">
	<thead>
		<tr>
			<th>Pin</th>
			<th>Ring of fire</th>
			<th>FRC Digital Sidecar</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>Ground</td>
			<td>Power</td>
		</tr>
		<tr>
			<td>2</td>
			<td>I2C Clock</td>
			<td>I2C Clock</td>
		</tr>
		<tr>
			<td>3</td>
			<td>I2C Data</td>
			<td>I2C Data</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Power</td>
			<td>Ground</td>
		</tr>
	</tbody>
</table>
