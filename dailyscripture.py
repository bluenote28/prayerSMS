import os
import random
from twilio.rest import Client



scripture = [
    "“Do not think that I have come to abolish the law and the prophets; I have come not to abolish them but to fulfil them. For truly, I say to you, till heaven and earth pass away, not an iota, not a dot, will pass from the law until all is accomplished. Whoever then relaxes one of the least of these commandments and teaches men so, shall be called least in the kingdom of heaven; but he who does them and teaches them shall be called great in the kingdom of heaven. For I tell you, unless your righteousness exceeds that of the scribes and Pharisees, you will never enter the kingdom of heaven.",
    "Seeing the crowds, he went up on the mountain, and when he sat down his disciples came to him. And he opened his mouth and taught them, saying: “Blessed are the poor in spirit, for theirs is the kingdom of heaven. “Blessed are those who mourn, for they shall be comforted. “Blessed are the meek, for they shall inherit the earth. “Blessed are those who hunger and thirst for righteousness, for they shall be satisfied. “Blessed are the merciful, for they shall obtain mercy. “Blessed are the pure in heart, for they shall see God. “Blessed are the peacemakers, for they shall be called sons of God. “Blessed are those who are persecuted for righteousness’ sake, for theirs is the kingdom of heaven. “Blessed are you when men revile you and persecute you and utter all kinds of evil against you falsely on my account. Rejoice and be glad, for your reward is great in heaven, for so men persecuted the prophets who were before you.",
    "“Not every one who says to me, ‘Lord, Lord,’ shall enter the kingdom of heaven, but he who does the will of my Father who is in heaven. On that day many will say to me, ‘Lord, Lord, did we not prophesy in your name, and cast out demons in your name, and do many mighty works in your name?’ And then will I declare to them, ‘I never knew you; depart from me, you evildoers.’ Hearers and Doers “Every one then who hears these words of mine and does them will be like a wise man who built his house upon the rock; and the rain fell, and the floods came, and the winds blew and beat upon that house, but it did not fall, because it had been founded on the rock. And every one who hears these words of mine and does not do them will be like a foolish man who built his house upon the sand; and the rain fell, and the floods came, and the winds blew and beat against that house, and it fell; and great was the fall of it.” And when Jesus finished these sayings, the crowds were astonished at his teaching, for he taught them as one who had authority, and not as their scribes.",
    "Now when Jesus saw great crowds around him, he gave orders to go over to the other side. And a scribe came up and said to him, “Teacher, I will follow you wherever you go.” And Jesus said to him, “Foxes have holes, and birds of the air have nests; but the Son of man has nowhere to lay his head.” Another of the disciples said to him, “Lord, let me first go and bury my father.” But Jesus said to him, “Follow me, and leave the dead to bury their own dead.”",
    "And Jesus went away from there and withdrew to the district of Tyre and Si'don. And behold, a Canaanite woman from that region came out and cried, “Have mercy on me, O Lord, Son of David; my daughter is severely possessed by a demon.” But he did not answer her a word. And his disciples came and begged him, saying, “Send her away, for she is crying after us.” He answered, “I was sent only to the lost sheep of the house of Israel.” But she came and knelt before him, saying, “Lord, help me.” And he answered, “It is not fair to take the children’s bread and throw it to the dogs.” She said, “Yes, Lord, yet even the dogs eat the crumbs that fall from their masters’ table.” Then Jesus answered her, “O woman, great is your faith! Let it be done for you as you desire.” And her daughter was healed instantly.",
    "Then Jesus told his disciples, “If any man would come after me, let him deny himself and take up his cross and follow me. For whoever would save his life will lose it, and whoever loses his life for my sake will find it. For what will it profit a man, if he gains the whole world and forfeits his life? Or what shall a man give in return for his life? For the Son of man is to come with his angels in the glory of his Father, and then he will repay every man for what he has done. Truly, I say to you, there are some standing here who will not taste death before they see the Son of man coming in his kingdom.”",
    "Now when Jesus came into the district of Caesare'a Philip'pi, he asked his disciples, “Who do men say that the Son of man is?” And they said, “Some say John the Baptist, others say Eli'jah, and others Jeremiah or one of the prophets.”He said to them, “But who do you say that I am?” Simon Peter replied, “You are the Christ, the Son of the living God.” And Jesus answered him, “Blessed are you, Simon Bar-Jona! For flesh and blood has not revealed this to you, but my Father who is in heaven. And I tell you, you are Peter, and on this rock I will build my Church, and the gates of Hades shall not prevail against it. I will give you the keys of the kingdom of heaven,and whatever you bind on earth shall be bound in heaven, and whatever you loose on earth shall be loosed in heaven.” Then he strictly charged the disciples to tell no one that he was the Christ.",
    "And when they came to the crowd, a man came up to him and kneeling before him said, “Lord, have mercy on my son, for he is an epileptic and he suffers terribly; for often he falls into the fire, and often into the water. And I brought him to your disciples, and they could not heal him.” And Jesus answered, “O faithless and perverse generation, how long am I to be with you? How long am I to bear with you? Bring him here to me.” And Jesus rebuked him, and the demon came out of him, and the boy was cured instantly. Then the disciples came to Jesus privately and said, “Why could we not cast it out?” He said to them, “Because of your little faith. For truly, I say to you, if you have faith as a grain of mustard seed, you will say to this mountain, ‘Move from here to there,’ and it will move; and nothing will be impossible to you.”",
    "When Jesus had spoken these words, he lifted up his eyes to heaven and said, “Father, the hour has come; glorify your Son that the Son may glorify you, since you have given him power over all flesh, to give eternal life to all whom you have given him. And this is eternal life, that they know you the only true God, and Jesus Christ whom you have sent. I glorified you on earth, having accomplished the work which you gave me to do; and now, Father, glorify me in your own presence with the glory which I had with you before the world was made.",
    "Now among those who went up to worship at the feast were some Greeks. So these came to Philip, who was from Beth-sa'ida in Galilee, and said to him, “Sir, we wish to see Jesus.” Philip went and told Andrew; Andrew went with Philip and they told Jesus. And Jesus answered them, “The hour has come for the Son of man to be glorified. Truly, truly, I say to you, unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit. He who loves his life loses it, and he who hates his life in this world will keep it for eternal life. If any one serves me, he must follow me; and where I am, there shall my servant be also; if any one serves me, the Father will honor him.",
    "Again Jesus spoke to them, saying, “I am the light of the world; he who follows me will not walk in darkness, but will have the light of life.” The Pharisees then said to him, “You are bearing witness to yourself; your testimony is not true.” Jesus answered, “Even if I do bear witness to myself, my testimony is true, for I know where I have come from and where I am going, but you do not know where I come from or where I am going. You judge according to the flesh, I judge no one. Yet even if I do judge, my judgment is true, for it is not I alone that judge, but I and hes who sent me. In your law it is written that the testimony of two men is true; I bear witness to myself, and the Father who sent me bears witness to me.” They said to him therefore, “Where is your Father?” Jesus answered, “You know neither me nor my Father; if you knew me, you would know my Father also.” These words he spoke in the treasury, as he taught in the temple; but no one arrested him, because his hour had not yet come.",
    "And a ruler asked him, “Good Teacher, what shall I do to inherit eternal life?” And Jesus said to him, “Why do you call me good? No one is good but God alone. You know the commandments: ‘Do not commit adultery, Do not kill, Do not steal, Do not bear false witness, Honor your father and mother.’” And he said, “All these I have observed from my youth.” And when Jesus heard it, he said to him, “One thing you still lack. Sell all that you have and distribute to the poor, and you will have treasure in heaven; and come, follow me.” But when he heard this he became sad, for he was very rich. Jesus looking at him said, “How hard it is for those who have riches to enter the kingdom of God! For it is easier for a camel to go through the eye of a needle than for a rich man to enter the kingdom of God.” Those who heard it said, “Then who can be saved?” But he said, “What is impossible with men is possible with God.” And Peter said, “Behold, we have left our homes and followed you.” And he said to them, “Truly, I say to you, there is no man who has left house or wife or brothers or parents or children, for the sake of the kingdom of God, who will not receive manifold more in this time, and in the age to come eternal life.”",
    "And he told them a parable, to the effect that they ought always to pray and not lose heart. He said, “In a certain city there was a judge who neither feared God nor regarded man; 3and there was a widow in that city who kept coming to him and saying, ‘Vindicate me against my adversary.’ For a while he refused; but afterward he said to himself, ‘Though I neither fear God nor regard man, yet because this widow bothers me, I will vindicate her, or she will wear me out by her continual coming.’” And the Lord said, “Hear what the unrighteous judge says. And will not God vindicate his elect, who cry to him day and night? Will he delay long over them? I tell you, he will vindicate them speedily. Nevertheless, when the Son of man comes, will he find faith on earth?”",
    "And Sad'ducees came to him, who say that there is no resurrection; and they asked him a question, saying, “Teacher, Moses wrote for us that if a man’s brother dies and leaves a wife, but leaves no child, the man must take the wife, and raise up children for his brother. There were seven brothers; the first took a wife, and when he died left no children; and the second took her, and died, leaving no children; and the third likewise; 22and the seven left no children. Last of all the woman also died. In the resurrection whose wife will she be? For the seven had her as wife.” Jesus said to them, “Is not this why you are wrong, that you know neither the Scriptures nor the power of God? For when they rise from the dead, they neither marry nor are given in marriage, but are like angels in heaven. And as for the dead being raised, have you not read in the book of Moses, in the passage about the bush, how God said to him, ‘I am the God of Abraham, and the God of Isaac, and the God of Jacob’? He is not God of the dead, but of the living; you are quite wrong.”",
    "For God so loved the world that he gave his only-begotten Son, that whoever believes in him should not perish but have eternal life. For God sent the Son into the world, not to condemn the world, but that the world might be saved through him. He who believes in him is not condemned; he who does not believe is condemned already, because he has not believed in the name of the only-begotten Son of God.",
    "As Jesus passed on from there, he saw a man called Matthew sitting at the tax office; and he said to him, “Follow me.” And he rose and followed him. And as he sat at table in the house, behold, many tax collectors and sinners came and sat down with Jesus and his disciples. And when the Pharisees saw this, they said to his disciples, “Why does your teacher eat with tax collectors and sinners?” But when he heard it, he said, “Those who are well have no need of a physician, but those who are sick. Go and learn what this means, ‘I desire mercy, and not sacrifice.’ For I came not to call the righteous, but sinners.”"
]



scripture_choice = random.randrange(len(scripture) - 1)


account_sid = os.environ['account_sid'] #twilio account sid environment variable
auth_token = os.environ['auth_token'] #twilio authorization token environment variable
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=scripture[scripture_choice],
  from_="+", #add twilio account phone number
  to="+" #add your phone number
)