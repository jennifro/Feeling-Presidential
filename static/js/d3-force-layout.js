var width = 900;
var height = 900;
var radius = 20;


var nodes = [
  {
    "group": 1,
    "id": "John F. Kennedy",
    "name": "John F. Kennedy"
  },
  {
    "group": 1,
    "id": "Lyndon B. Johnson",
    "name": "Lyndon B. Johnson"
  },
  {
    "group": 1,
    "id": "Richard Nixon",
    "name": "Richard Nixon"
  },
  {
    "group": 1,
    "id": "Jimmy Carter",
    "name": "Jimmy Carter"
  },
  {
    "group": 1,
    "id": "Gerald Ford",
    "name": "Gerald Ford"
  },
  {
    "group": 1,
    "id": "Ronald Reagan",
    "name": "Ronald Reagan"
  },
  {
    "group": 1,
    "id": "George H. W. Bush",
    "name": "George H. W. Bush"
  },
  {
    "group": 1,
    "id": "Bill Clinton",
    "name": "Bill Clinton"
  },
  {
    "group": 1,
    "id": "George W. Bush",
    "name": "George W. Bush"
  },
  {
    "group": 1,
    "id": "Barack Obama",
    "name": "Barack Obama"
  },
  {
    "group": 2,
    "id": "Inaugural Address (January 20, 1961)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 14, 1963)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union (January 8, 1964)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 22, 1970)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "First Inaugural Address (January 20, 1969)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "Inaugural Address (January 20, 1965)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 11, 1962)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 14, 1969)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 30, 1974)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "Inaugural Address (January 20, 1977)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 19, 1978)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 15, 1975)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "Remarks on Taking the Oath of Office (August 9, 1974)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 23, 1980)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 12, 1977)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 25, 1988)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "First Inaugural Address (January 20, 1981)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 26, 1982)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "Inaugural Address (January 20, 1989)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 31, 1990)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 28, 1992)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "First Inaugural (January 20, 1993)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 27, 2000)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 25, 1994)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "First Inaugural Address (January 20, 2001)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 29, 2002)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "Inaugural Address (January 20, 2009)",
    "name": "I"
  },
  {
    "group": 2,
    "id": "2016 State of the Union Address (January 12, 2016)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "State of the Union Address (January 28, 2008)",
    "name": "SotU"
  },
  {
    "group": 2,
    "id": "2010 State of the Union Address (January 27, 2010)",
    "name": "SotU"
  },
  {
    "group": 5,
    "id": "cut capital",
    "name": "cut capital"
  },
  {
    "group": 5,
    "id": "strong america",
    "name": "strong america"
  },
  {
    "group": 5,
    "id": "capital gains",
    "name": "capital gains"
  },
  {
    "group": 5,
    "id": "health care",
    "name": "health care"
  },
  {
    "group": 5,
    "id": "interest rates",
    "name": "interest rates"
  },
  {
    "group": 5,
    "id": "toughest neighborhoods",
    "name": "toughest neighborhoods"
  },
  {
    "group": 4,
    "id": "eastern europe",
    "name": "eastern europe"
  },
  {
    "group": 5,
    "id": "human rights",
    "name": "human rights"
  },
  {
    "group": 4,
    "id": "al qaeda",
    "name": "al qaeda"
  },
  {
    "group": 5,
    "id": "america must",
    "name": "america must"
  },
  {
    "group": 5,
    "id": "united states",
    "name": "united states"
  },
  {
    "group": 4,
    "id": "america best",
    "name": "america best"
  },
  {
    "group": 5,
    "id": "trust fund",
    "name": "trust fund"
  },
  {
    "group": 5,
    "id": "finish job",
    "name": "finish job"
  },
  {
    "group": 5,
    "id": "smallbusiness owners",
    "name": "smallbusiness owners"
  },
  {
    "group": 5,
    "id": "persian gulf",
    "name": "persian gulf"
  },
  {
    "group": 4,
    "id": "strengthen nation",
    "name": "strengthen nation"
  },
  {
    "group": 5,
    "id": "renew america",
    "name": "renew america"
  },
  {
    "group": 5,
    "id": "wall street",
    "name": "wall street"
  },
  {
    "group": 4,
    "id": "fellow citizens",
    "name": "fellow citizens"
  },
  {
    "group": 5,
    "id": "balance payments",
    "name": "balance payments"
  },
  {
    "group": 5,
    "id": "new breeze",
    "name": "new breeze"
  },
  {
    "group": 5,
    "id": "side side",
    "name": "side side"
  },
  {
    "group": 5,
    "id": "personal privacy",
    "name": "personal privacy"
  },
  {
    "group": 5,
    "id": "7 years",
    "name": "7 years"
  },
  {
    "group": 5,
    "id": "tax relief",
    "name": "tax relief"
  },
  {
    "group": 5,
    "id": "cutting back",
    "name": "cutting back"
  },
  {
    "group": 5,
    "id": "left behind",
    "name": "left behind"
  },
  {
    "group": 5,
    "id": "rate inflation",
    "name": "rate inflation"
  },
  {
    "group": 5,
    "id": "balanced budget",
    "name": "balanced budget"
  },
  {
    "group": 4,
    "id": "soviet union",
    "name": "soviet union"
  },
  {
    "group": 4,
    "id": "middle east",
    "name": "middle east"
  },
  {
    "group": 4,
    "id": "holy land",
    "name": "holy land"
  },
  {
    "group": 4,
    "id": "state union",
    "name": "state union"
  },
  {
    "group": 5,
    "id": "set aside",
    "name": "set aside"
  },
  {
    "group": 5,
    "id": "health insurance",
    "name": "health insurance"
  },
  {
    "group": 5,
    "id": "let sides",
    "name": "let sides"
  },
  {
    "group": 5,
    "id": "middle class",
    "name": "middle class"
  },
  {
    "group": 5,
    "id": "last year",
    "name": "last year"
  },
  {
    "group": 5,
    "id": "surplus capacity",
    "name": "surplus capacity"
  },
  {
    "group": 5,
    "id": "public life",
    "name": "public life"
  },
  {
    "group": 4,
    "id": "working families",
    "name": "working families"
  },
  {
    "group": 5,
    "id": "civil rights",
    "name": "civil rights"
  },
  {
    "group": 5,
    "id": "nearly half",
    "name": "nearly half"
  },
  {
    "group": 5,
    "id": "weve got",
    "name": "weve got"
  },
  {
    "group": 5,
    "id": "third century",
    "name": "third century"
  },
  {
    "group": 5,
    "id": "foreign policy",
    "name": "foreign policy"
  },
  {
    "group": 5,
    "id": "party lines",
    "name": "party lines"
  },
  {
    "group": 5,
    "id": "latin america",
    "name": "latin america"
  },
  {
    "group": 4,
    "id": "new world",
    "name": "new world"
  },
  {
    "group": 5,
    "id": "50 percent",
    "name": "50 percent"
  },
  {
    "group": 5,
    "id": "12 percent",
    "name": "12 percent"
  },
  {
    "group": 5,
    "id": "every american",
    "name": "every american"
  },
  {
    "group": 5,
    "id": "real estate",
    "name": "real estate"
  },
  {
    "group": 5,
    "id": "mass destruction",
    "name": "mass destruction"
  },
  {
    "group": 5,
    "id": "go forward",
    "name": "go forward"
  },
  {
    "group": 5,
    "id": "september 11",
    "name": "september 11"
  },
  {
    "group": 5,
    "id": "freedom fighters",
    "name": "freedom fighters"
  },
  {
    "group": 5,
    "id": "natural gas",
    "name": "natural gas"
  },
  {
    "group": 5,
    "id": "home abroad",
    "name": "home abroad"
  },
  {
    "group": 5,
    "id": "april 1",
    "name": "april 1"
  },
  {
    "group": 4,
    "id": "atlantic community",
    "name": "atlantic community"
  },
  {
    "group": 5,
    "id": "fellow americans",
    "name": "fellow americans"
  },
  {
    "group": 5,
    "id": "local governments",
    "name": "local governments"
  },
  {
    "group": 5,
    "id": "major step",
    "name": "major step"
  },
  {
    "group": 5,
    "id": "breeze blowing",
    "name": "breeze blowing"
  },
  {
    "group": 5,
    "id": "new engagement",
    "name": "new engagement"
  },
  {
    "group": 5,
    "id": "cost living",
    "name": "cost living"
  },
  {
    "group": 5,
    "id": "men women",
    "name": "men women"
  },
  {
    "group": 5,
    "id": "hard times",
    "name": "hard times"
  },
  {
    "group": 5,
    "id": "prescription drugs",
    "name": "prescription drugs"
  },
  {
    "group": 5,
    "id": "federal government",
    "name": "federal government"
  },
  {
    "group": 5,
    "id": "across party",
    "name": "across party"
  },
  {
    "group": 5,
    "id": "status quo",
    "name": "status quo"
  },
  {
    "group": 5,
    "id": "mr speaker",
    "name": "mr speaker"
  },
  {
    "group": 5,
    "id": "tonight announcing",
    "name": "tonight announcing"
  },
  {
    "group": 5,
    "id": "white house",
    "name": "white house"
  },
  {
    "group": 5,
    "id": "welfare programs",
    "name": "welfare programs"
  },
  {
    "group": 4,
    "id": "union depends",
    "name": "union depends"
  },
  {
    "group": 5,
    "id": "american hostages",
    "name": "american hostages"
  },
  {
    "group": 4,
    "id": "cannot afford",
    "name": "cannot afford"
  },
  {
    "group": 5,
    "id": "let us",
    "name": "let us"
  },
  {
    "group": 5,
    "id": "law enforcement",
    "name": "law enforcement"
  },
  {
    "group": 5,
    "id": "years ago",
    "name": "years ago"
  },
  {
    "group": 5,
    "id": "cold war",
    "name": "cold war"
  },
  {
    "group": 5,
    "id": "forward together",
    "name": "forward together"
  },
  {
    "group": 5,
    "id": "go away",
    "name": "go away"
  },
  {
    "group": 5,
    "id": "nuclear weapons",
    "name": "nuclear weapons"
  },
  {
    "group": 5,
    "id": "members public",
    "name": "members public"
  },
  {
    "group": 5,
    "id": "grass roots",
    "name": "grass roots"
  },
  {
    "group": 5,
    "id": "new spirit",
    "name": "new spirit"
  },
  {
    "group": 5,
    "id": "executive branch",
    "name": "executive branch"
  }
];

var links = [
    {
      "source": "John F. Kennedy",
      "target": "Inaugural Address (January 20, 1961)",
      "type": "prez-speech"
    },
    {
      "source": "John F. Kennedy",
      "target": "State of the Union Address (January 14, 1963)",
      "type": "prez-speech"
    },
    {
      "source": "Lyndon B. Johnson",
      "target": "State of the Union (January 8, 1964)",
      "type": "prez-speech"
    },
    {
      "source": "Richard Nixon",
      "target": "State of the Union Address (January 22, 1970)",
      "type": "prez-speech"
    },
    {
      "source": "Richard Nixon",
      "target": "First Inaugural Address (January 20, 1969)",
      "type": "prez-speech"
    },
    {
      "source": "Lyndon B. Johnson",
      "target": "Inaugural Address (January 20, 1965)",
      "type": "prez-speech"
    },
    {
      "source": "John F. Kennedy",
      "target": "State of the Union Address (January 11, 1962)",
      "type": "prez-speech"
    },
    {
      "source": "Lyndon B. Johnson",
      "target": "State of the Union Address (January 14, 1969)",
      "type": "prez-speech"
    },
    {
      "source": "Richard Nixon",
      "target": "State of the Union Address (January 30, 1974)",
      "type": "prez-speech"
    },
    {
      "source": "Jimmy Carter",
      "target": "Inaugural Address (January 20, 1977)",
      "type": "prez-speech"
    },
    {
      "source": "Jimmy Carter",
      "target": "State of the Union Address (January 19, 1978)",
      "type": "prez-speech"
    },
    {
      "source": "Gerald Ford",
      "target": "State of the Union Address (January 15, 1975)",
      "type": "prez-speech"
    },
    {
      "source": "Gerald Ford",
      "target": "Remarks on Taking the Oath of Office (August 9, 1974)",
      "type": "prez-speech"
    },
    {
      "source": "Jimmy Carter",
      "target": "State of the Union Address (January 23, 1980)",
      "type": "prez-speech"
    },
    {
      "source": "Gerald Ford",
      "target": "State of the Union Address (January 12, 1977)",
      "type": "prez-speech"
    },
    {
      "source": "Ronald Reagan",
      "target": "State of the Union Address (January 25, 1988)",
      "type": "prez-speech"
    },
    {
      "source": "Ronald Reagan",
      "target": "First Inaugural Address (January 20, 1981)",
      "type": "prez-speech"
    },
    {
      "source": "Ronald Reagan",
      "target": "State of the Union Address (January 26, 1982)",
      "type": "prez-speech"
    },
    {
      "source": "George H. W. Bush",
      "target": "Inaugural Address (January 20, 1989)",
      "type": "prez-speech"
    },
    {
      "source": "George H. W. Bush",
      "target": "State of the Union Address (January 31, 1990)",
      "type": "prez-speech"
    },
    {
      "source": "George H. W. Bush",
      "target": "State of the Union Address (January 28, 1992)",
      "type": "prez-speech"
    },
    {
      "source": "Bill Clinton",
      "target": "First Inaugural (January 20, 1993)",
      "type": "prez-speech"
    },
    {
      "source": "Bill Clinton",
      "target": "State of the Union Address (January 27, 2000)",
      "type": "prez-speech"
    },
    {
      "source": "Bill Clinton",
      "target": "State of the Union Address (January 25, 1994)",
      "type": "prez-speech"
    },
    {
      "source": "George W. Bush",
      "target": "First Inaugural Address (January 20, 2001)",
      "type": "prez-speech"
    },
    {
      "source": "George W. Bush",
      "target": "State of the Union Address (January 29, 2002)",
      "type": "prez-speech"
    },
    {
      "source": "Barack Obama",
      "target": "Inaugural Address (January 20, 2009)",
      "type": "prez-speech"
    },
    {
      "source": "Barack Obama",
      "target": "2016 State of the Union Address (January 12, 2016)",
      "type": "prez-speech"
    },
    {
      "source": "George W. Bush",
      "target": "State of the Union Address (January 28, 2008)",
      "type": "prez-speech"
    },
    {
      "source": "Barack Obama",
      "target": "2010 State of the Union Address (January 27, 2010)",
      "type": "prez-speech"
    },
    {
      "source": "State of the Union Address (January 14, 1969)",
      "target": "local governments",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "middle east",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1969)",
      "target": "set aside",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 30, 1974)",
      "target": "soviet union",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1969)",
      "target": "executive branch",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union (January 8, 1964)",
      "target": "cutting back",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural (January 20, 1993)",
      "target": "fellow americans",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union (January 8, 1964)",
      "target": "side side",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union (January 8, 1964)",
      "target": "members public",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union (January 8, 1964)",
      "target": "every american",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 22, 1970)",
      "target": "cost living",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 22, 1970)",
      "target": "50 percent",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "balanced budget",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 22, 1970)",
      "target": "law enforcement",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 12, 1977)",
      "target": "third century",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1969)",
      "target": "go forward",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1969)",
      "target": "forward together",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "let us",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "middle east",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "soviet union",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "health care",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 30, 1974)",
      "target": "personal privacy",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "state union",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "middle class",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1994)",
      "target": "toughest neighborhoods",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1994)",
      "target": "weve got",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "interest rates",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1994)",
      "target": "white house",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "party lines",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "across party",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "mr speaker",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "prescription drugs",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "finish job",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "fellow americans",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 27, 2000)",
      "target": "let us",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural (January 20, 1993)",
      "target": "renew america",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural (January 20, 1993)",
      "target": "new world",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural (January 20, 1993)",
      "target": "america must",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1989)",
      "target": "breeze blowing",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1989)",
      "target": "new engagement",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1989)",
      "target": "new breeze",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1989)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 31, 1990)",
      "target": "home abroad",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 31, 1990)",
      "target": "eastern europe",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 31, 1990)",
      "target": "tonight announcing",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 31, 1990)",
      "target": "union depends",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 1992)",
      "target": "capital gains",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 2009)",
      "target": "men women",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 1992)",
      "target": "cut capital",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 1992)",
      "target": "real estate",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 1992)",
      "target": "hard times",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 11, 1962)",
      "target": "balance payments",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 11, 1962)",
      "target": "health insurance",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 11, 1962)",
      "target": "strong america",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 11, 1962)",
      "target": "latin america",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 11, 1962)",
      "target": "atlantic community",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1961)",
      "target": "fellow citizens",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1961)",
      "target": "let sides",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1961)",
      "target": "let us",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1963)",
      "target": "cold war",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1963)",
      "target": "men women",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1963)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1963)",
      "target": "cannot afford",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 14, 1963)",
      "target": "strengthen nation",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "natural gas",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "april 1",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "surplus capacity",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "12 percent",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "middle east",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "third century",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 15, 1975)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 12, 1977)",
      "target": "years ago",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 12, 1977)",
      "target": "state union",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "persian gulf",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "american hostages",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "nuclear weapons",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "middle east",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 23, 1980)",
      "target": "last year",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1977)",
      "target": "new spirit",
      "type": "speech-bigram"
    },
    {
      "source": "Inaugural Address (January 20, 1977)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 19, 1978)",
      "target": "major step",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 19, 1978)",
      "target": "human rights",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 19, 1978)",
      "target": "rate inflation",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "foreign policy",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 2001)",
      "target": "america best",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 29, 2002)",
      "target": "mass destruction",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 29, 2002)",
      "target": "september 11",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 29, 2002)",
      "target": "men women",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "tax relief",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "holy land",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "left behind",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "men women",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 28, 2008)",
      "target": "tax relief",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "status quo",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "civil rights",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "middle class",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "smallbusiness owners",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "wall street",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "men women",
      "type": "speech-bigram"
    },
    {
      "source": "2010 State of the Union Address (January 27, 2010)",
      "target": "let us",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "al qaeda",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "public life",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "united states",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "working families",
      "type": "speech-bigram"
    },
    {
      "source": "2016 State of the Union Address (January 12, 2016)",
      "target": "health care",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "go away",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "federal government",
      "type": "speech-bigram"
    },
    {
      "source": "First Inaugural Address (January 20, 1981)",
      "target": "let us",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "grass roots",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "trust fund",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "nearly half",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "interest rates",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "foreign policy",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 26, 1982)",
      "target": "state union",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "welfare programs",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "balanced budget",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "freedom fighters",
      "type": "speech-bigram"
    },
    {
      "source": "State of the Union Address (January 25, 1988)",
      "target": "7 years",
      "type": "speech-bigram"
    }
];


var svg = d3.select("#force").append('svg')
    .attr('width', width)
    .attr('height', height);

var force = d3.layout.force()
  .size([width, height])
  .nodes(nodes)
  .links(links);


var simulation = d3.forceSimulation()
    .velocityDecay(0.15)
    .force("link", d3.forceLink().distance(10).id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-100))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collide", d3.forceCollide(function(d) { return d.r + 30; }).strength(0.9).iterations(16))
    .force("x", d3.forceX(0))
    .force("y", d3.forceY(0));


var color = {
    1: 'rgb(9, 33, 64)',
    2: 'rgb(242, 71, 56)',
    3: 'rgb(5, 166, 76)',
    4: 'rgb(2, 73, 89)',
    5: 'rgb(191, 42, 42)' };

var sizes = {1: 16, 2: 3, 3: 5, 4: 5, 5: 5 };

var cirColor = {
    1: 'rgb(9, 33, 64)',
    2: 'rgb(242, 71, 56',
    3: 'rgb(5, 166, 76)',
    4: 'rgb(2, 73, 89)',
    5: 'rgb(191, 42, 42)' };

var fontSize = {
    1: 20,
    2: 12,
    3: 14,
    4: 14,
    5: 14 };

var linkWidth = {
    "prez-speech": 2,
    "speech-bigram": 1.5
};

var linkColor = {
    "prez-speech": 'rgb(9, 33, 64)',
    "speech-bigram": 'rgb(242, 71, 56)'
};

var link = svg.append("g").selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .attr("class", function(d) { return "link " + d.type; })
    .style('stroke-width', function(d) { return linkWidth[d.type]; })
    .style("stroke", function(d) { return linkColor[d.type]; });
  // .attr("stroke-width", '1px');

var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("r", function(d) { return sizes[d.group]; })
    .attr("fill", function(d) { return cirColor[d.group]; })
    .attr('class', function(d) { return 'node' + d.group; })
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

node.append("title")
    .text(function(d) { return d.id; });

var text = svg.append("g").selectAll("text")
    .data(graph.nodes)
    .enter().append("text")
    .attr("dx", 5)
    .attr("dy", ".31em")
    .attr('text-anchor', 'start')
    .text(function(d) { return d.name; })
    .attr('class', function(d) { return 'text' + d.group; })
    .style('fill', function(d) { return color[d.group]; })
    .style('font-size', function(d) { return fontSize[d.group]; });

    // node.append("image")
    //  .attr("xlink:href", function(d) { return d.icon; })
    //   .attr("x", "-12px")
    //   .attr("y", "-12px")
    //   .attr("width", "24px")
    //   .attr("height", "24px");

simulation
    .nodes(graph.nodes)
    .on("tick", ticked);

simulation.force("link")
    .links(graph.links);


function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

    text
        .attr("x", function (d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("y", function (d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

     // node.each(collide(0.5));
}


function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}