<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
    <h2>Dummy Code Book</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
	  <!-- Table Heathers -->
        <th>Variable</th>
		<th>Note</th>
        <th>Coding</th>
		<th>Statistics</th>
      </tr>
      <xsl:for-each select="This_CodeBook/Variable">
      <tr>
		<!-- Variable Name -->
        <td><xsl:value-of select="Name" /></td>
		<!-- Variable Note -->
		<td><p><xsl:value-of select="Note" /></p></td>
		<!-- Variable Code -->
		<td>
		<table border="1">
		<tr bgcolor="#9acd32">
			<td>Code</td>
			<td>Value</td>
		</tr>
		<tr>
		<xsl:for-each select="Coding/Code">
			<tr>
				<td><xsl:value-of select="Name" /></td>
				<td><xsl:value-of select="Value" /></td>
			</tr>
		</xsl:for-each>
		</tr>
		</table>
		</td>
		<!-- Variable Statistics -->
		<td>
		<table border="1">
		<tr bgcolor="#9acd32">
			<td>Code</td>
			<td>Value</td>
		</tr>
		<tr>
		<xsl:for-each select="Statistics/Statistic">
			<tr>
				<td><xsl:value-of select="Name" /></td>
				<td><xsl:value-of select="Value" /></td>
			</tr>
		</xsl:for-each>
		</tr>
		</table>
		</td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>