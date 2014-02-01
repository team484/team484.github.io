---
title: Missing java.util.Math functions
layout: post
---

We needed the advanced math functions that are in `java.lang.Math`, but they aren't there!  NetBeans knows to not auto-complete, but we really don't want to write our own
versions.

The problem is that we are not using the full Java VM, but a limited &quot;Squawk&quot; version.

Fortunately, the latest versions have an implementation in [com.sun.squawk.util.MathUtils](http://www.sunspotworld.com/docs/Yellow/javadoc/com/sun/squawk/util/MathUtils.html).
It includes `asin`, `atan`, `exp`, `pow` and `log` among others.
