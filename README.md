<html>
  <head>
  </head>
  <body>
    <h1>Data Analysis With Insights</h1>
    <h4>
      Data Analysis has become an integral part of the stepping stone towards data science.
      <a href="https://jayforsk.herokuapp.com/" target="_blank">view project</a>
    </h4>
    <div>
     Presenting a Web application using a Python Sciprt with Dash framework, displaying data visualization of global terrorism using a dataset of approximately 1,90,000 records. 
    </div>
    <h5>Two Types of visualization have been used:</h5>
    <ul>
      <li>
        World Map Plot
        <ul>
          <li>World Map Plot</li>
          <li>India Specific Plot</li>
        </ul>
      </li>
      <li>
        Area Chart
        <ul>
          <li>World Area Chart - showing number of incident counts every year.</li>
          <li>India Specific Area Chart - showing number of incident counts every year.</li>
        </ul>
      </li>
    </ul>
    <h3>Map UI</h3>
    <div>
      There are seven dropdown UI each of which plays the function of a filter for the world plot.
    </div>
    <div>The Dropdown UIs are:
      <ul>
        <li>Month</li>
        <li>Date</li>
        <li>Region</li>
        <li>Country</li>
        <li>Province/State</li>
        <li>City</li>
        <li>Attack-Type</li>
      </ul>
      There are restrictions that like the user has to select month first and then day. First you have to select Region then countries of that particular selected region. This filtering of the country based on the region is done using auto filtering callbacks. Similarly State and then city has the same effect.
    </div>
    <div>
      The World Map Plot has a legend beside it showing the attacktype whether Bombing, Armed Assault, etc.
    </div>
    <div><b>India Specific Map Plot -</b> The Region is fixed and set to South Asia and the country is set to India. In addition if one wants to apply filters based on Month, Day, State, City, AttackType the user can apply and see the updated results. This updation of the map is done using callbacks of the particular component based on its 'id'. The legend is same as the World Map PLot </div>
    <div>
      <h3>Chart Tool</h3>
      <div>The Chart Tool has world chart tool and India specific chart tool</div>
      <h3>Chart Tool UI</h3>
      <div>
        <ul>
          <li>Incidents Grouped By- Region(by default)</li>
          <li>Search Box Filter</li>
          <li>Area Chart</li>
        </ul>
      </div>
      <div>
        The dropdown filter which groups incidents based on dropdown value. This is also the legend of the Area Chart.
      </div>
      <div>
        The Search searches for the selected dropdown filter's content, whether it is contained in it or not. If it yields results then they are shown, if not the original legend is shown that has been selected from the dropdown.
      </div>
      <div>
        <b>India Specific Area Chart -</b> has the region and country selected as 'South Asia' and 'India' by default and then the dropdown filter is applied on it. If the user searches for something then it is showed or else shows the legend of dropdown selected filter.
      </div>
    </div>
    
  </body>
</html>


